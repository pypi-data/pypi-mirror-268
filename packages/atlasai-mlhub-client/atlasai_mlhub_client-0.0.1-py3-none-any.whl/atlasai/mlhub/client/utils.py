import os

def validate_request_headers(headers):
    if not headers.get('Authorization'):
        raise Exception('No Authorization token found. Authenticate first')


def get_headers():
    headers = {"Content-Type": "application/json"}

    if os.getenv('MLHUB_TOKEN'):
        headers['Authorization'] = f'Bearer {os.getenv("MLHUB_TOKEN")}'

    validate_request_headers(headers)
    return headers

def get_model_url(model, version):
    return f"{get_base_url()}/model/{model}/version/{version}"

def get_base_url():
    return f"{os.environ['MLHUB_URL']}"
