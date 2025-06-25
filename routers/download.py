from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from routers.upload import get_file_map

router = APIRouter(tags=["File Download"])

@router.get("/download-file/{download_id}")
async def download_file(download_id: str):
    file_map = get_file_map()
    file_path = file_map.get(download_id)

    if not file_path:
        raise HTTPException(status_code=404, detail="Assignment ID not found")

    return FileResponse(
        path=file_path,
        filename=file_path.split("/")[-1],
        media_type="application/octet-stream"
    )
