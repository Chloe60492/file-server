# utils/azure_config.py
import os
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

load_dotenv()

def get_container_client():
    connection_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    container_name = os.getenv("AZURE_CONTAINER_NAME", "files")
    blob_service_client = BlobServiceClient.from_connection_string(connection_str)
    container_client = blob_service_client.get_container_client(container_name)

    try:
        container_client.create_container()
    except Exception:
        pass

    return container_client
