from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from app.routers import user

import os

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# for ssl certificate
# put XXXXX.txt to backend/app/static
@app.get("/.well-known/pki-validation/{ssl_file_name}", response_class=FileResponse)
def ssl(ssl_file_name: str):
    ssl_file_path = f"backend/app/static/{ssl_file_name}"
    print(ssl_file_name)

    return FileResponse(path=ssl_file_path, filename=ssl_file_name, media_type="text")




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



@app.get("/")
def read_root():
    return {"Hello": "World!"}
