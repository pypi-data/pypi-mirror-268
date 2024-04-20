import httpx
from tenacity import retry, stop_after_attempt, wait_random_exponential

httpx_client: tuple = None, None
from parrot_api.core import log_event
from datetime import datetime, timezone


def get_client(sync=False):
    import httpx
    from datetime import datetime, timedelta
    global httpx_client
    now = datetime.utcnow()
    if httpx_client[1] is not sync or httpx_client[0] is None or httpx_client[2] < (now - timedelta(hours=1)):
        if not sync:
            httpx_client = httpx.AsyncClient(http2=True, follow_redirects=True), sync, now
        else:
            httpx_client = httpx.Client(http2=True, follow_redirects=True), sync, now
    return httpx_client[0]


def format_response_body(response):
    js = dict()
    try:
        js = response.json()
    except ValueError:
        js['content'] = response.text
    return js


def safe_json_request(method, url, stop=stop_after_attempt(3), reraise=True, sync=False, filtered_response_keys=None,
                      raise_over=500, wait=wait_random_exponential(multiplier=.01, max=1), log_attributes=None,
                      **kwargs):
    client = get_client(sync=sync)
    if log_attributes is None:
        log_attributes = {k: v for k, v in kwargs.items() if kwargs not in ['headers']}
    if filtered_response_keys is None:
        filtered_response_keys = []
    log_event(
        level='info', status='success', process_type='request_created', payload=dict(
            method=method,
            url=url,
            created_ts=datetime.now(tz=timezone.utc).timestamp(),
            **log_attributes
        )
    )
    args = dict(
        client=client, method=method, url=url, stop=stop, reraise=reraise, wait=wait,
        filtered_response_keys=filtered_response_keys, raise_over=raise_over,
        log_attributes=log_attributes, **kwargs
    )
    if sync:
        return sync_safe_json_request(**args)
    else:
        return async_safe_json_request(**args)


async def async_safe_json_request(client, method, url, log_attributes, filtered_response_keys, raise_over, reraise,
                                  stop, wait, **kwargs):
    import httpx
    @retry(stop=stop, reraise=reraise, wait=wait)
    async def make_async_request():
        resp = await client.request(method=method, url=url, **kwargs)
        status, json_response = process_response(
            url=url, resp=resp, method=method, raise_over=raise_over,
            log_attributes=log_attributes, filtered_response_keys=filtered_response_keys
        )
        return status, json_response

    try:
        status_code, js = await make_async_request()
    except (httpx.RequestError, httpx.HTTPStatusError) as exc:
        status_code, js = process_errors(
            url=url, exc=exc, method=method, log_attributes=log_attributes
        )
    return status_code, js


def sync_safe_json_request(client, method, url, log_attributes, filtered_response_keys, raise_over, reraise,
                           stop, wait, **kwargs):
    import httpx
    @retry(stop=stop, reraise=reraise, wait=wait)
    def make_sync_request():
        resp = client.request(method=method, url=url, **kwargs)
        status, json_response = process_response(
            url=url, resp=resp, method=method, raise_over=raise_over,
            log_attributes=log_attributes, filtered_response_keys=filtered_response_keys
        )
        return status, json_response

    try:
        status_code, js = make_sync_request()
    except (httpx.RequestError, httpx.HTTPStatusError) as exc:
        status_code, js = process_errors(
            url=url, exc=exc, method=method, log_attributes=log_attributes
        )
    return status_code, js


def process_response(method, url, resp, raise_over, filtered_response_keys, log_attributes):
    status = resp.status_code
    js = format_response_body(response=resp)
    level = 'info' if status < 400 else 'error'
    status_level = 'success' if status < raise_over else 'failure'
    log_event(
        level=level, status=status_level, process_type='request_completed', payload=dict(
            method=method,
            url=url,
            status=status,
            created_ts=datetime.now(tz=timezone.utc).timestamp(),
            **log_attributes,
            **{k: v for k, v in js.items() if k not in filtered_response_keys}
        )
    )
    if status >= raise_over:
        resp.raise_for_status()
    return status, js


def process_errors(exc, method, url, log_attributes):
    status_code, js = None, dict()
    if isinstance(exc, httpx.RequestError):
        log_event(
            level='error', status='failure', process_type='request_completed', payload=dict(
                method=method,
                url=url,
                status=status_code,
                created_ts=datetime.now(tz=timezone.utc).timestamp(),
                **log_attributes,
            )
        )
    elif isinstance(exc, httpx.HTTPStatusError):
        js = format_response_body(response=exc.response)
        status_code = exc.response.status_code
    return status_code, js


def generate_oauth_headers(access_token: str) -> dict:
    """Convenience function to generate oauth stand authorization header

    :param access_token: Oauth access token
    :return: Request headers
    """
    return {'Authorization': 'Bearer ' + access_token}
