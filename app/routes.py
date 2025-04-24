
from fastapi import APIRouter, File, UploadFile, HTTPException
from pathlib import Path
from uuid import uuid4
from app.utils import recognize_face_in_image

from app.utils import save_and_process_image

router = APIRouter()

@router.post("/register/")
async def register_user(name: str,image: UploadFile= File(...)):
    return save_and_process_image(name,image)





@router.post("/recognize/")
async def recognize_face(image: UploadFile = File(...)):
    # Save upload to disk
    temp_path = Path("uploads") / f"{uuid4()}.jpg"
    with open(temp_path, "wb") as buf:
        buf.write(await image.read())

    # Run recognition
    result = recognize_face_in_image(temp_path)
    if result.get("status") == "error":
        raise HTTPException(status_code=400, detail=result["detail"])
    return result
