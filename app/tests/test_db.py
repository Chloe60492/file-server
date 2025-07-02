# tests/test_azure_connection.py
import os
from azure.core.exceptions import AzureError
from azure.storage.blob import BlobServiceClient
from app.config import AZURE_CONNECTION_STRING, AZURE_CONTAINER_NAME

def test_azure_storage_connection():
    # Ensure environment variables are loaded
    connection_str = AZURE_CONNECTION_STRING
    container_name = AZURE_CONTAINER_NAME

    try:
        
        blob_service_client = BlobServiceClient.from_connection_string(connection_str)
        container_client = blob_service_client.get_container_client(container_name)

        # Check container client is created
        # print(blob_service_client)
        

        # Optional: Try listing blobs to confirm connection
        blobs = list(container_client.list_blobs())
        # print(blobs)
        print("Connection successfully!")

    except AzureError as e:
        print(f"AzureError occurred: {str(e)}")

    except Exception as e:
        print(f"Unexpected error occurred: {str(e)}")

if __name__ == '__main__':
    test_azure_storage_connection()