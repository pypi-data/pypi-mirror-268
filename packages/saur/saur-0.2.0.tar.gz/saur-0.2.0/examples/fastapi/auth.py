# pylint: disable=missing-module-docstring,missing-function-docstring,missing-class-docstring
# adapted from https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/

from datetime import timedelta, datetime
from typing import Annotated

# pip install python-jose[cryptography] passlib[bcrypt]
from fastapi import HTTPException, Depends, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound
from pydantic import BaseModel

from saur.app.fastapi import Session

from .models import User
from .schemas import UserCreateSchema, UserWritableSchema

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: int | None = None

class UserSchema(BaseModel):
    id: int
    email: str

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

async def get_user(session: AsyncSession, email: str):
    try:
        return (await User.find(session=session, email=email)).one()
    except NoResultFound:
        return None

async def authenticate_user(session: AsyncSession, email: str, password: str) -> User | None:
    user = await get_user(session=session, email=email)
    if user is None:
        return None
    if not verify_password(password, user.passhash):
        return None
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

async def get_current_user(session: Session, token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        token_data = TokenData(user_id=user_id)
    except JWTError:
        raise credentials_exception  # pylint: disable=raise-missing-from
    user = await get_user(session, email=token_data.username)
    if user is None:
        raise credentials_exception
    return user

CurrentUser = Annotated[User, Depends(get_current_user)]

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/token", response_model=Token)
async def login_for_access_token(
    session: Session,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = await authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.user_id}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@auth_router.get("/user")
async def read_user(current_user: CurrentUser) -> UserSchema:
    return current_user

@auth_router.put("/user", status_code=status.HTTP_205)
async def update_user(session: Session, current_user: CurrentUser, user: UserWritableSchema):
    user_data = user.model_dump()
    new_password = user_data.pop('password')
    if new_password is not None:
        user_data['passhash'] = get_password_hash(new_password)
    current_user.update(**user_data)
    await session.commit()

@auth_router.post("/user", status_code=status.HTTP_200_OK)
async def create_user(session: Session, user: UserCreateSchema) -> UserSchema:
    user_data = user.model_dump()
    user_data['passhash'] = get_password_hash(user_data.pop('password'))
    new_user = User.create(session=session, **user_data)
    await session.commit()
    return new_user

@auth_router.delete("/user", status_code=status.HTTP_205)
async def delete(session: Session, current_user: CurrentUser):
    await current_user.delete(session)
