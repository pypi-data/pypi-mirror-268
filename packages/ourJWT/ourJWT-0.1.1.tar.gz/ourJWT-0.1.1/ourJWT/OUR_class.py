import jwt

from . import OUR_exception
from django.http import HttpRequest, response

good_iss = "OUR_Transcendence"

class HttpResponseUnauthorized(response.HttpResponse):
    status_code = 401

class Decoder:
    pub_key: str

    def __init__(self, pub_key):
        if pub_key is None:
             raise OUR_exception.NoKey
        Decoder.pub_key = pub_key


    @staticmethod
    def decode(to_decode, check_date: bool=True):
        """
        decode the given JWT into a dict.

        Args:
            to_decode (str): The JWT to be decoded.

        Raises:
            OUR_exception.BadSubject: If the type is not "refresh" or "auth".
            OUR_exception.RefusedToken: If the token is invalid
            OUR_exception.ExpiredToken: if the token is expired

        Returns:
            dict: The decoded JWT.
        """
        try:
            token = jwt.decode(jwt=to_decode,
                                key=Decoder.pub_key,
                                algorithms=["RS256"],
                                issuer=good_iss,
                                options={"verify_exp": check_date})
        except(jwt.DecodeError,
                jwt.InvalidIssuerError,
                jwt.InvalidSignatureError):
            raise OUR_exception.RefusedToken()
        except jwt.ExpiredSignatureError:
            raise OUR_exception.ExpiredToken()
        if token["sub"] != "auth" and token["sub"] != "refresh":
            raise OUR_exception.BadSubject
        return token

    def check_auth():
        def decorator(function):
            def wrapper(request: HttpRequest):
                auth: str = request.COOKIES.get("auth_token", None)
                if auth is None:
                    return response.HttpResponseBadRequest(reason="No auth cookie sent")
                try:
                    auth_decoded = Decoder.decode(auth)
                except (OUR_exception.BadSubject,
                        OUR_exception.RefusedToken,
                        OUR_exception.ExpiredToken):
                    return HttpResponseUnauthorized(reason="Bad auth token")
                return function(request, token=auth_decoded)
            return wrapper
        return decorator




class Encoder:
    private_key: str

    def __init__(self, priv_key):
        if priv_key is None:
            raise OUR_exception.NoKey
        self.private_key = priv_key

    def encode(self, to_encode, type):
        """
        Encodes the given payload into a JWT (JSON Web Token).

        Args:
            to_encode (dict): The payload to be encoded into the JWT.
            type (str): The type of the token, must be either "refresh" or "auth".

        Raises:
            OUR_exception.BadSubject: If the type is not "refresh" or "auth".
            TypeError: If the payload is not a dictionary.

        Returns:
            str: The encoded JWT.
        """
        if type != "refresh" and type != "auth":
            raise OUR_exception.BadSubject()
        if self.private_key is None:
            raise OUR_exception.NoKey()
        if not isinstance(to_encode, dict):
            raise TypeError("Payload not a dict")
        to_encode["iss"] = good_iss
        to_encode["sub"] = type
        encoded = jwt.encode(payload=to_encode,
                             key=self.private_key,
                             algorithm="RS256")
        return encoded
