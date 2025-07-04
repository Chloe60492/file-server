# routes/attachment.py
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse
from app.crud import attachment
from fastapi import Query
from typing import Optional

router = APIRouter(prefix="/attachments", tags=["Attachments"])

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return await attachment.upload_file_to_blob(file)

@router.get("/download")
def download_file(filename: Optional[str] = Query(None)):
    return attachment.download_blob_file(filename)

@router.get("/list")
def list_files():
    return attachment.list_blob_files()

@router.delete("/delete/{filename:path}")
def delete_file(filename: str):
    return attachment.delete_blob_file(filename)
