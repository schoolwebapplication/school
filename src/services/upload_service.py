from fastapi_app import app
from fastapi import APIRouter, UploadFile
import os
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent

if not os.path.isdir(f"{ROOT}/UPLOADS"):
    os.mkdir(f"{ROOT}/UPLOADS")

upload_router = APIRouter(prefix="/upload_file")


@upload_router.get("")
async def get_info():
    return {}


@upload_router.post("")
async def upload_doc(file: UploadFile):
    # print(__file__.name)
    print(type(file))
    print(f'file name is {file.filename}')
    contents = await file.read()
    file.close()
    with open(f'{ROOT}/UPLOADS/{file.filename}', 'wb') as f:
        f.write(contents)
    return {f"file is successfully uploaded"}


app.include_router(upload_router)





