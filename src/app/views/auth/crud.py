from datetime import timedelta, datetime

import jwt
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer

from passlib.context import CryptContext
from sqlalchemy.orm import Session

from src.app.views.auth.model import UserResponse
from src.app.db.models.users import UserDTO

SECRET_KEY = "6fae1ef0cfecd0dca91324cf854c4730f335ded08c6b4686264a85688e470faa"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def decode_jwt(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Необходимо войти в систему",
            headers={"Authorization": "Bearer"},
        )


def get_current_user(session: Session, token: str = Depends(oauth2_scheme)) -> UserResponse:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Необходимо войти в систему",
        headers={"Authorization": "Bearer"},
    )

    payload = decode_jwt(token)
    if payload is None:
        raise credentials_exception

    user_login = payload.get("sub")
    if user_login is None:
        raise credentials_exception

    user = session.get(UserDTO, user_login)
    if user is None:
        raise credentials_exception

    return UserResponse.from_orm(user)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


