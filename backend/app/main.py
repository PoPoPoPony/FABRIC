from fastapi import FastAPI, Depends
from app.schemas.user import UserInfo
from app.utils.auth import get_current_user
from fastapi.middleware.cors import CORSMiddleware
from app.routers import user


# auth 的所有需要的組件都先寫在utils.auth中，所以router也在裡面
from app.utils import auth

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
app.include_router(auth.router)






@app.get("/me", response_model=UserInfo)
async def read_users_me(current_user: UserInfo = Depends(get_current_user)):
    return current_user


@app.get("/")
def read_root():
    return {"Hello": "World!"}
