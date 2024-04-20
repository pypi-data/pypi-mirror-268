import requests

from s3i.exception import S3IDittoError, raise_error_from_ditto_response


def query_all(fn):
    """Adds pagination to a request.

    Expects a function, that returns a rest get request without the keyword "cursor".
    Returns a list of json objects, that meet the query.

    :param fn: Function returning a rest get request
    :type fn: function
    """
    def inner(*args, **kwargs):
        url, headers = fn(*args, **kwargs)
        response = requests.get(url, headers=headers)
        raise_error_from_ditto_response(response, S3IDittoError, 200)
        results = response.json().get("items")
        cursor = response.json().get("cursor")
        while cursor:
            response = requests.get(url,
                                    headers=headers,
                                    params={"option": f"cursor({cursor})"})
            raise_error_from_ditto_response(response, S3IDittoError, 200)
            items = response.json()["items"]
            results += items
            cursor = response.json().get("cursor", None)
        return results

    return inner


