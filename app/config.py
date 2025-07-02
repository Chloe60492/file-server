# app/config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Loads from project-root/.env by default

AZURE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
AZURE_CONTAINER_NAME = os.getenv("AZURE_CONTAINER_NAME", "files")
# print(AZURE_CONNECTION_STRING, AZURE_CONTAINER_NAME)