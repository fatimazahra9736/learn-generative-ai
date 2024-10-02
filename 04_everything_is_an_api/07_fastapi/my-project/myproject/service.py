from passlib.context import CryptContext
from datetime import timedelta, datetime, timezone  
from jose import  jwt, JWTError
from typing import Annotated
from fastapi import Header , HTTPException , status
from myproject.model.model import TokenData

SECRET_KEY = "090e3ba2a1d93d843715cb8cec50e1730e20991c62b04e7e249ef9b378d1490c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

a = 'token:  authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InN0cmluZyIsImlkIjoxLCJleHAiOjE3MjU1NTMyNjR9.1F8Nfdu8uKPzitdF-6S59aWbWrQyYRlNQiMpdbeiIZY '


pwd_context  = CryptContext(schemes=["bcrypt"] , deprecated="auto")

def hashed_pass(password):
    return pwd_context.hash(password)

def verify_pass(userpass , dbpass):
    return pwd_context.verify(userpass ,  dbpass)

def create_token(data:dict , expire_delta:timedelta | None = None ):
    to_encode = data.copy()
    if expire_delta:
        expire = datetime.now(timezone.utc) + expire_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes= 15)
    to_encode.update({"exp" : expire})
    encode_jwt = jwt.encode(to_encode , SECRET_KEY , algorithm = ALGORITHM)
    return encode_jwt

def verify_token(token:Annotated[str , Header()]):
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="Could not validate credentials f" , headers={"WWW-Authenticat":"Bearer"})
    try:
        payload = jwt.decode(token , SECRET_KEY , algorithms = ALGORITHM)
        email:str | None = payload.get("email")
        id:str | None = payload.get("id")
        if email is None:
           raise exception 
        else:
            yield TokenData(email=email , id=id)
    except JWTError: 
        raise exception