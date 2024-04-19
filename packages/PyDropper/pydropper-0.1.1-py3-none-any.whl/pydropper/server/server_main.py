from fastapi import FastAPI, File, UploadFile, status
from fastapi.responses import JSONResponse
import aiofiles
from ..env import STORAGE_PATH

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/upload")
async def store_image(file: UploadFile = File(...)):
    destination = f"{STORAGE_PATH}/{file.filename}"
    async with aiofiles.open(destination, "wb") as f:
        await f.write(await file.read())
    return JSONResponse(
        status_code=status.HTTP_200_OK, content={"message": "File uploaded"}
    )
