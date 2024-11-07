from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Config:
    """Class to manage configuration settings."""
    
    HISTORY_FILE_PATH = os.getenv('HISTORY_FILE_PATH', 'default_history_path.txt')  # Default path if not set
    LOG_FILE_PATH = os.getenv('LOG_FILE_PATH', 'default_log_path.txt')  # Default path if not set

    def __init__(self):
        # You can add more initialization if needed
        pass 