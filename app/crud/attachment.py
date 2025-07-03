# crud/attachment.py
from fastapi import UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from app.utils.azure_config import get_container_client

container_client = get_container_client()

async def upload_file_to_blob(file: UploadFile):
    try:
        data = await file.read()
        if not data:
            raise HTTPException(status_code=400, detail="Empty file.")
        blob_client = container_client.get_blob_client(file.filename)
        blob_client.upload_blob(data, overwrite=True)
        return {"message": f"File '{file.filename}' uploaded."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def download_blob_file(filename: str):
    try:
        blob_client = container_client.get_blob_client(filename)
        stream = blob_client.download_blob()
        return StreamingResponse(stream.chunks(), media_type="application/octet-stream")
    except Exception:
        raise HTTPException(status_code=404, detail="File not found.")

def list_blob_files():
    try:
        return [blob.name for blob in container_client.list_blobs()]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# def delete_blob_file(filename: str):
#     try:
#         blob_client = container_client.get_blob_client(filename)
#         blob_client.delete_blob()
#         return {"message": f"File '{filename}' deleted."}
#     except Exception:
#         raise HTTPException(status_code=404, detail="File not found.")
def delete_blob_file(filename: str):
    try:
        blobs = [blob.name for blob in container_client.list_blobs()]
        if filename not in blobs:
            raise HTTPException(status_code=404, detail=f"Blob '{filename}' not found.")
        blob_client = container_client.get_blob_client(filename)
        blob_client.delete_blob()
        return {"message": f"File '{filename}' deleted."}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

