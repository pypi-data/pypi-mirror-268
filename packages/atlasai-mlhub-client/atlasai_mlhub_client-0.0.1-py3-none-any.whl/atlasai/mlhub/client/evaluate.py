import concurrent.futures
import logging
import os
import time
from typing import Union

from .constants import DEPLOYMENT_TYPES, DEFAULT_POLLING_TIMEOUT, POLLING_INTERVAL
from .requests import get_session
from .response import JobResultResponse, JobResponse
from .utils import get_headers, get_model_url

logger = logging.getLogger(__name__)

def evaluate(
        model: str, version: str, data: dict = None,
        deployment_type: str = DEPLOYMENT_TYPES.http,
        timeout: int = DEFAULT_POLLING_TIMEOUT,
        wait_for_completion: bool = True
) -> Union[JobResultResponse, JobResponse]:
    """
    Evaluate a specific model with specific data.

    Args:
        model (str): The name of the model you want to evaluate
        version (str): The version of the model you want to evaluate
        deployment_type (str): The type of deployment you want. http or batch.

        data (dict): The data to be sent in the request body.
        timeout (int, optional): Maximum time interval to wait for a response
        wait_for_completion (bool, optional, default: true). Wait for the function to poll for results in case of batch.
            Set to false in case you want to do the polling yourself.

    Returns:
        JobResultResponse: The response object from the evaluation.
        JobResponse: If batch deployment type is true and wait_for_completion is false will return a string with the resource to poll.

    """

    if not os.environ['MLHUB_URL']:
        raise ValueError('MLHUB_URL must be provided.')

    url = f"{get_model_url(model, version)}/evaluate"

    headers = get_headers()

    body = {
        'deployment_type': deployment_type,
        'version': version,
        'data': data
    }
    session = get_session()
    response = session.post(url, json=body, headers=headers, timeout=timeout)
    response.raise_for_status()

    if response.status_code == 200:
        return JobResultResponse.from_dict(**response.json())
    elif response.status_code == 202:
        if wait_for_completion:
            return process_polling_response(model, version, response.headers['Location'], timeout=timeout)
        else:
            return JobResponse(model=model, version=version, job_id=response.headers['Location'])



def get_job_result(data: JobResponse, timeout: int = DEFAULT_POLLING_TIMEOUT):
    """
    Get results for a specific job

    Args:
        data: JobResponse. Object that contains the model, version and resource to poll

        timeout (int, optional): Maximum time interval to wait for a response

    Returns:
        JobResultResponse: The response object from the evaluation.

    """
    if not os.environ['MLHUB_URL']:
        raise ValueError('MLHUB_URL must be provided.')

    session = get_session()

    headers = get_headers()
    url = f"{get_model_url(data.model, data.version)}/job/{data.job_id}"
    response = session.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()

    if response.status_code == 200:
        return JobResultResponse.from_dict(**response.json())


def process_polling_response(model, version, job_id, timeout=DEFAULT_POLLING_TIMEOUT):
    def poll(_url):
        while True:
            headers = get_headers()
            session = get_session()
            _response = session.get(_url, headers=headers)
            _response.raise_for_status()

            data = _response.json()
            status = data.get("status")
            if status != "InProgress":
                return data

            time.sleep(POLLING_INTERVAL)

    def poll_until_finished(_url):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(poll, _url)
            try:
                done, _ = concurrent.futures.wait([future], timeout=timeout)
                for f in done:
                    return f.result()
            except concurrent.futures.TimeoutError:
                future.cancel()
                raise Exception("Polling timeout")
            except Exception as e:
                logger.error(f"Polling failed: {e}")
                raise e

    url = f"{get_model_url(model, version)}/job/{job_id}"

    response = poll_until_finished(url)
    return JobResultResponse.from_dict(**response)
