import logging
import os

LOG_FILE = os.getenv('LOG_FILE_PATH', 'logs/leetcode.log')

# Create file if it doesn't exists
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# Create a custom logger
logger = logging.getLogger("leetcode")
logger.setLevel(logging.DEBUG)  # Set the root logger level to DEBUG

# File Handler: Logs everything (INFO, DEBUG, and ERROR)
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Console Handler: Logs only INFO and ERROR
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Show INFO and above (INFO, ERROR, etc.)
console_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(console_formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)