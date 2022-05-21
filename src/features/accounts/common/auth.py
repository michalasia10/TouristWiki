import time
from typing import Dict

import jwt
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import EmailStr

from src.core.settings import CREDENTIALS


def token_response(token: str):
    return {
        'TOKEN': token
    }


def sign_jwt(email: EmailStr, credential_type: str) -> Dict[str, str]:
    payload = {
        'email': email,
        'expires': time.time() + 2400,
        'credentials': credential_type
    }
    return token_response(jwt.encode(payload, credential_type, algorithm='HS256'))


def decode_jwt(token: str, credential_type) -> dict:
    decoded_token = jwt.decode(token.encode(), credential_type, algorithms=["HS256"])

    if decoded_token['expires'] >= time.time() or decoded_token['credentials'] in CREDENTIALS[credential_type]:
        return decoded_token

    return {}


class JWTBearer(HTTPBearer):
    def __init__(self, credentials_type: str, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)
        self._credentials_type = credentials_type

    async def __call__(self, request: Request):
        credentialns: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentialns:
            if not credentialns.scheme == 'Bearer':
                raise HTTPException(
                    status_code=403,
                    detail="Invalid or Expired Token!"
                )
            return credentialns.credentials
        raise HTTPException(
            status_code=403,
            detail="Invalid or Expired Token!"
        )

    def verify_jwt(self, jwtoken: str):
        return bool(decode_jwt(jwtoken, self._credentials_type))
