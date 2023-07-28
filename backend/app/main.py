from fastapi import FastAPI
from fastapi.responses import FileResponse
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