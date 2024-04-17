"""
## Helpers for Requests package
"""

import requests
from requests.adapters import HTTPAdapter, Retry
from .utils import get_headers

STATUS_FORCELIST = tuple([429, 500, 502, 503, 504])

def mount_retry(
    session,
    total=10,
    backoff_factor=0.2,
    allowed_methods=None,
    status_forcelist=STATUS_FORCELIST,
):
    """
    Attach retry handlers to HTTP and HTTPS endpoints of a Requests Session
    """

    retries = Retry(
        total=total,
        backoff_factor=backoff_factor,
        allowed_methods=allowed_methods,
        status_forcelist=status_forcelist,
    )

    session.mount('http://', HTTPAdapter(max_retries=retries))
    session.mount('https://', HTTPAdapter(max_retries=retries))

def get_session(
    total=10,
    backoff_factor=0.2,
    allowed_methods=None,
    status_forcelist=STATUS_FORCELIST,
):
    """
    Get a Requests Session with retry handlers for HTTP and HTTPS endpoints
    """

    sess = requests.Session()
    mount_retry(
        sess,
        total=total,
        backoff_factor=backoff_factor,
        allowed_methods=allowed_methods,
        status_forcelist=status_forcelist,
    )

    return sess

def paginate(url, limit=100, offset=0):
    def _get_results(_url, _limit, _offset):
        _response = session.post(_url, json={'limit': _limit, 'offset': _offset}, headers=get_headers())
        _response.raise_for_status()
        return _response

    results = []
    session = get_session()
    while True:
        response = _get_results(url, limit, offset)
        data = response.json()['data']
        if not data:
            break
        results.extend(data)
        offset += limit
    return results
