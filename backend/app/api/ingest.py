from fastapi import APIRouter, HTTPException, UploadFile, File
import shutil
import os
from backend import ROOT_PATH

router = APIRouter()

UPLOAD_PATH = os.path.join(ROOT_PATH, "..", "data", "uploads")


@router.post("/ingest/upload")
async def upload_file(
    file: UploadFile = File(...),
):  # File(...) tells FastAPI that parameter should be taken from a file upload in a request
    if not file.filename.endswith(".csv"):
        raise HTTPException(
            status_code=400, detail="Invalid file type. Only .csv files are allowed."
        )
    os.makedirs(UPLOAD_PATH, exist_ok=True)
    file_path = os.path.join(UPLOAD_PATH, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "file_path": file_path}
