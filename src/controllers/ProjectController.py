from .BaseController import BaseController
from fastapi import UploadFile
from src.models import ResoponseSignal
import os

class ProjectController(BaseController):
    def __init__(self):
        super().__init__()

    # A function to create a directory for the file with the project_id number
    def get_project_path(self, project_id: str):
        '''
        returns the project directory
        '''
        project_dir = os.path.join(
            self.files_dir,
            project_id
        )
        # check if path exists
        if not os.path.exists(project_dir):
            os.makedirs(project_dir)

        return project_dir