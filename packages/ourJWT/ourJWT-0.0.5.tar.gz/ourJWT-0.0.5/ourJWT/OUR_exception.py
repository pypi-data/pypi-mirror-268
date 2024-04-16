class RefusedToken(Exception):
    def __str__(self):
        return "Cannot decode Token"


class ExpiredToken(Exception):
    def __str__(self):
        return "token has expired"


class NoKey(Exception):
    def __str__(self):
        return "Couldn't locate public/private key"

class BadSubject(Exception):
    def __str__(self):
        return "Bad subject in token"
