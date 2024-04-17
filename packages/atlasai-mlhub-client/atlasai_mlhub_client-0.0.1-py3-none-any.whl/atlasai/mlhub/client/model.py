import logging

from .requests import get_session, paginate
from .response import ModelInfoResponse, ModelResponse, ModelResponses
from .utils import get_base_url, get_headers, get_model_url


logger = logging.getLogger(__name__)

def get_models(limit=100, offset=0):
    url = f"{get_base_url()}/models"

    results = paginate(url, limit, offset)

    return ModelResponses(responses=[ModelResponse.from_dict(**result) for result in results])


def get_model_info(model, version):
    url = get_model_url(model, version)

    session = get_session()

    response = session.get(url, headers=get_headers())
    response.raise_for_status()

    return ModelInfoResponse.from_dict(**response.json())
