from fastapi import APIRouter, File, UploadFile, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from utils.file_validator import validate_file_type
import os
import uuid

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

router = APIRouter(prefix="/ops", tags=["File Upload"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# Store file references in-memory for download lookup
file_map = {}

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post("/upload-file")
async def upload_file(file: UploadFile = File(...), username: str = Depends(get_current_user)):
    if not validate_file_type(file.filename):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only .pptx, .docx, and .xlsx files allowed."
        )

    os.makedirs("uploads", exist_ok=True)

    download_id = str(uuid.uuid4())
    file_path = f"uploads/{download_id}_{file.filename}"

    contents = await file.read()
    with open(file_path, "wb") as f:
        f.write(contents)

    # Store in map for retrieval
    file_map[download_id] = file_path

    return {
        "download-link": f"http://127.0.0.1:8000/download-file/{download_id}",
        "message": "success"
    }

# Expose this for use in download.py
def get_file_map():
    return file_map
