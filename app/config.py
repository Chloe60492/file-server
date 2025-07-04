# app/config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Loads from project-root/.env by default

AZURE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
AZURE_CONTAINER_NAME = os.getenv("AZURE_CONTAINER_NAME", "files")
FILE_SERVER_URL = os.getenv("FILE_SERVER_URL")
print(AZURE_CONNECTION_STRING, AZURE_CONTAINER_NAME, FILE_SERVER_URL)