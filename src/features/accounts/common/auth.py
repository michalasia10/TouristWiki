import time
from typing import Dict
import jwt


def token_response(token: str):
    return {
        'access_token': token
    }


def sign_jwt(user_id: str) -> Dict[str, str]:
    payload = {
        'user_id': user_id,
        'expires': time.time() + 2400
    }
    return token_response(jwt.encode(payload, 'DUMMY', algorithm='HS256'))


def decode_jwt(token: str) -> dict:
    decoded_token = jwt.decode(token.encode(), 'DUMMY', algorithms=["HS256"])
    return decoded_token if decoded_token['expires'] >= time.time() else {}
