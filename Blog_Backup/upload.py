from fastapi import FastAPI, UploadFile, File, Form
import shutil
import os

app = FastAPI()

@app.post("/upload")
async def create_upload_file(file: UploadFile = File(...)):
    with open(os.path.join("/www/wwwroot/http/xunlei/files", file.filename), "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename, "stats": "上传成功" }

@app.post("/delete")
async def delete_file(filename: str = Form(...)):
    file_path = os.path.join("/www/wwwroot/http/xunlei/files", filename)
    if os.path.isfile(file_path):
        os.remove(file_path)
        return {"filename": filename, "status": "删除成功"}
    else:
        return {"filename": filename, "status": "文件未找到"}