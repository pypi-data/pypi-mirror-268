import logging

from .requests import paginate
from .response import JobInfoResponse, JobInfoResponses
from .utils import get_model_url


logger = logging.getLogger(__name__)

def get_jobs(model, version, limit=100, offset=0):
    url = f"{get_model_url(model, version)}/jobs"

    results = paginate(url, limit, offset)

    return JobInfoResponses(jobs=[JobInfoResponse.from_dict(**result) for result in results])
