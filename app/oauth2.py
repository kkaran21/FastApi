from datetime import datetime, timedelta
from fastapi import Depends, HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt,JWTError
from . import schemas
from .config import settings

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY=settings.secret_key
ALGORITHM=settings.algorithm
EXPIRATION_TIME=settings.token_expiration_time_minutes

def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=EXPIRATION_TIME)
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,ALGORITHM)

    return encoded_jwt

def verify_access_token(token:str=Depends(oauth2_scheme)):

    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},)

    try:
        payload=jwt.decode(token,SECRET_KEY,[ALGORITHM])
        id=payload.get("id")
        email=payload.get("email")

        if id and email is None:
            raise credentials_exception
        token_data=schemas.TokenData(id=id,email=email)

    except JWTError:
        raise credentials_exception
    return token_data

