from src.helpers.config import get_settings, Settings
import os
import random
import string


class BaseController:
    
    def __init__(self):
        self.app_settings = get_settings()
        
        self.base_dir = os.path.dirname(os.path.dirname(__file__)) #get the dir path of src folder
        
        self.file_dir = os.path.join(self.base_dir, "assets/files")
        
        
    def generate_random_string(self, length: int=12):
        # Combine lowercase, uppercase letters, and digits
        characters = string.ascii_letters + string.digits
        
        # Randomly choose characters and join them into a string
        return ''.join(random.choice(characters) for _ in range(length))    
        
        