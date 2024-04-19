import json
import urllib
import requests
from zvolv_sdk import user_defined_exceptions


def handle_request(func):
    def wrapper_func(*args, **kwargs):
        query_params = kwargs.get("query_params")
        if query_params:
            updated_query_params = [(k, str(v).lower() if isinstance(v, bool) else v) for k, v in query_params.items()]
            encoded_query_params = urllib.urlencode(updated_query_params)
            kwargs["rest_url"] += "?" + encoded_query_params
        headers = kwargs.get("headers")
        if headers is None:
            pass
        if kwargs.get("json"):
            kwargs["headers"].update({'Content-Type': 'application/json'})
            kwargs["data"] = json.dumps(kwargs["json"])
        ret_val = func(*args, **kwargs)
        return ret_val

    return wrapper_func


def handle_response(func):
    def wrapper_func(*args, **kwargs):
        ret_val = func(*args, **kwargs)
        status_code, response = ret_val.status_code, ret_val.text
        response_details = {"status_code": status_code, "response": response}
        response_details.update(kwargs)
        if status_code == 404:
            raise user_defined_exceptions.ResourceNotFound(message_details={"URL": kwargs.get("rest_url")})
        elif status_code == 500:
            raise user_defined_exceptions.InternalServerError(message_details={"URL": kwargs.get("rest_url")})
        elif status_code == 200:
            if json.loads(response).get("error"):
                raise user_defined_exceptions.InvalidRequest(
                    message_details={"error_message": json.loads(response).get("message")})
            return json.loads(response)
        else:
            return json.loads(response)

    return wrapper_func


@handle_request
@handle_response
def execute(rest_url, method, query_params=None, data=None, json=None, headers=None):
    """
    non-used params have manipulated in decorators.
    :param rest_url:
    :param method:
    :param query_params:
    :param data:
    :param json:
    :param headers:
    :return:
    """
    if method == "GET":
        return requests.get(url=rest_url, headers=headers)
    elif method == "POST":
        return requests.post(url=rest_url, data=data, headers=headers)
    elif method == "PUT":
        return requests.put(url=rest_url, data=data, headers=headers)