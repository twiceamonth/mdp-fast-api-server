

from fastapi import APIRouter, HTTPException, status

from src.app.views.auth.model import LoginResponse
from src.app.db.models.users import UserDTO
from src.app.db.base import convert_to_db
from src.app.db.db_connection import session as db

from src.app.views.auth.crud import hash_password, verify_password, create_access_token
from src.app.views.auth.model import UserCreate, UserInDb

router = APIRouter(tags=["Авторизация"])

@router.post("/register", response_model=UserInDb)
def register(user: UserCreate):
    hashed_password = hash_password(user.password_hash)
    db_user = convert_to_db(UserCreate(login=user.login, password_hash=hashed_password), UserDTO)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login", response_model=LoginResponse)
def login(user: UserCreate):
    db_user = db.query(UserDTO).filter(UserDTO.login == user.login).first()
    if not db_user or not verify_password(user.password_hash, db_user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный логин или пароль",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": db_user.login})
    return { "access_token": access_token, "token_type" : "Bearer"}