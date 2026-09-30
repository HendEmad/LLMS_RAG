from fastapi import APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
import os
from src.helpers.config import get_settings, Settings
from src.controllers import DataController, ProjectController  # will call init of controllers directly
import aiofiles
from src.models import ResoponseSignal
import logging

logger = logging.getLogger("uvicorn.error")
data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"] 
)

# end point to get the file and upload it to the system
@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile, 
                      app_settings: Settings=Depends(get_settings)):
    # validate the file properties
    # check file format to check allowed file type
    # check maximum size to check allowed max size
    data_controller = DataController()
    is_valid, result_signal = data_controller.validate_uploaded_file(file=file)
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": result_signal
            }
        )

    project_dir_path = ProjectController().get_project_path(project_id=project_id)  # create a directory for the uploaded file --> assets/files/project_id

    # save the file inside the directory created
    # file_path = os.path.join(
    #     project_dir_path,
    #     file.filename
    # )
    file_path, file_id = data_controller.generate_unique_filepath(
        orig_file_name=file.filename,
        project_id=project_id
    )

    # open the file by aiofiles lib --> to process it chunk by chunk
    try:
        async with aiofiles.open(file_path, "wb") as f:  # writing for all file types as binary
            # chunk by chunk
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)  # write the file chunk by chunk
    except Exception as e:
        # appear error in log in the system for the developer only, not for the user
        logger.error(f"Error while uploading file: {e}")

        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": ResoponseSignal.FILE_UPLOADED_FAILED.value
            }
        )

    return JSONResponse(
        content = {
            "signal": ResoponseSignal.FILE_UPLOADED_SUCCESS.value,
            "file_id": file_id
        }
    )