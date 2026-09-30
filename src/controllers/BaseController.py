# common settings and the remain controllers will inherit from it;
# the first common logic is get_settings, all of them will need the variables inside .env file
from src.helpers.config import get_settings, Settings
import os
import random
import string

class BaseController:
    def __init__(self):
        self.app_settings = get_settings()
        self.base_dir = os.path.dirname(os.path.dirname(__file__))  # current path
        self.files_dir = os.path.join(
            self.base_dir,
            "assets/files"
        )

    # create a unique random string
    def generate_random_string(self, length: int=12):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))