from django.http import HttpRequest, response

from . import OUR_exception, OUR_class


class HttpResponseUnauthorized(response.HttpResponse):
    status_code = 401


def auth_required(decoder: OUR_class.Decoder):
    def decorator(function):
        def wrapper(request: HttpRequest):
            auth: str = request.COOKIES.get("auth_token", None)
            if auth is None:
                return response.HttpResponseBadRequest(reason="No auth cookie sent")
            try:
                auth_decoded = decoder.decode(auth)
            except (OUR_exception.BadSubject,
                    OUR_exception.RefusedToken,
                    OUR_exception.ExpiredToken):
                return HttpResponseUnauthorized(reason="Bad auth token")
            return function(request, token=auth_decoded)
        return wrapper
    return decorator
