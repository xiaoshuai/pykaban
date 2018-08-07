def interpolate_str(template, **data):
    s = template
    for k, v in data.items():
        key = '{%' + k + '%}'
        s = s.replace(key, v)
    return s


def parser_response_content(response_content):
    import json
    from . import AzkabanClientException
    response_content = response_content.decode('utf-8')
    resp = json.loads(response_content)
    if 'error' in resp:
        error_message = resp['error']
        if 'message' in resp:
            error_message = error_message + '\n' + resp['message']
        raise AzkabanClientException(error_message)
    if 'status' in resp and resp['status'] == 'error':
        if 'message' in resp:
            error_message = resp['message']
        raise AzkabanClientException(error_message)
    return resp


