from fastapi import FastAPI, File, UploadFile, status
from fastapi.responses import JSONResponse
from os import makedirs
from aiofiles import open
from .config import STORAGE_PATH

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/upload")
async def store_image(file: UploadFile = File(...)):
    makedirs(STORAGE_PATH, exist_ok=True)
    destination = f"{STORAGE_PATH}/{file.filename}"
    async with open(destination, "wb") as f:
        await f.write(await file.read())
    return JSONResponse(
        status_code=status.HTTP_200_OK, content={"message": "File uploaded"}
    )
