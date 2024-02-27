from fastapi import FastAPI, UploadFile, File
import shutil
import os

app = FastAPI()

@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):
    with open(os.path.join("/", file.filename), "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename}