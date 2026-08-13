from fastapi import APIRouter, UploadFile, File, Depends
from services.cloudinary_service import upload_image
from auth.dependencies import get_current_admin

router = APIRouter()

@router.post("/image", dependencies=[Depends(get_current_admin)])
async def upload_thumbnail(file: UploadFile = File(...)):
    result_url = upload_image(file.file)
    return {"secure_url": result_url}