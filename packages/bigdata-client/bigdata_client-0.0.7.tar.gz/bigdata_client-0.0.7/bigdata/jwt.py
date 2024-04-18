import datetime

import jwt


def get_jwt_date(token: str, field: str) -> datetime.datetime:
    """
    Gets the expiration date of a token

    >>> token = jwt.encode({"iat": 1516239022}, "secret", algorithm="HS256")
    >>> get_jwt_date(token, "iat")
    datetime.datetime(2018, 1, 18, 1, 30, 22, tzinfo=datetime.timezone.utc)
    """
    header = jwt.decode(token, options={"verify_signature": False})
    timestamp = header[field]
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc)
