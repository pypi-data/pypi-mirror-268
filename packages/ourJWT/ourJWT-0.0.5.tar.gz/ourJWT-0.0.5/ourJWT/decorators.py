from django.http import HttpRequest, response

from . import OUR_exception, OUR_class


class HttpResponseUnauthorized(response.HttpResponse):
    status_code = 401


def auth_required(decoder: OUR_class.Decoder):
    def decorator(function):
        def wrapper(request: HttpRequest):
            auth: str = request.headers["Authorization"]
            if auth is None:
                return response.HttpResponseBadRequest(reason="No Authorization header found in request")
            auth_type = auth.split(" ")[0]
            if (auth_type) != "Bearer":
                return response.HttpResponseBadRequest(reason="Type not Bearer")
            auth_token = auth.split(" ")[1]
            if auth_token is None:
                return response.HttpResponseBadRequest(reason="No auth token detected")
            try:
                auth_decoded = decoder.decode(auth_token)
            except (OUR_exception.BadSubject,
                    OUR_exception.RefusedToken,
                    OUR_exception.ExpiredToken):
                return HttpResponseUnauthorized(reason="Bad auth token")
            return function(request, auth_decoded)
        return wrapper
    return decorator
