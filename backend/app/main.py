from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import FileResponse
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from app.routers import user
from app.utils import user as utils_user
from app.crud import user as crud_user
from app.schemas.user import UserData
from app.db.database import get_db

from datetime import datetime, timedelta
from typing import Annotated, Union
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from jose import JWTError, jwt
import hashlib

import os




# for ssl certificate
# put XXXXX.txt to backend/app/static
# @app.get("/.well-known/pki-validation/{ssl_file_name}", response_class=FileResponse)
# def ssl(ssl_file_name: str):
#     ssl_file_path = f"backend/app/static/{ssl_file_name}"
#     print(ssl_file_name)

#     return FileResponse(path=ssl_file_path, filename=ssl_file_name, media_type="text")




app = FastAPI()


# CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# app.include_router()
app.include_router(user.router)


JWT_SECRET = os.getenv("JWT_SECRET")
ALGORITHM = "HS512"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class Token(BaseModel):
    access_token: str
    token_type: str



def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)
    return encoded_jwt



async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        user_email: str = payload.get("sub")
        if user_email is None:
            raise credentials_exception
        # token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    db = next(get_db())
    user = crud_user.get_user(user_email, db)
    if user is None:
        raise credentials_exception
    return user


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    db = next(get_db())
    # username -> user_email, password -> frontend_hashed_pwd
    
    user = utils_user.authenticate_user(db, form_data.username, hashlib.sha512(str(form_data.password).encode("utf-8") ).hexdigest())
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.user_email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}



# @app.get("/me", response_model=UserInfo)
# async def read_users_me(current_user: UserInfo = Depends(get_current_user)):
#     return current_user


@app.get("/me")
async def read_users_me(current_user: UserData = Depends(get_current_user)):
    return current_user

@app.get("/")
def read_root():
    return {"Hello": "World!"}
