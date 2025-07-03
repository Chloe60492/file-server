# cli/utils.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("FILE_SERVER_URL")

def upload_file(file_path):
    """Upload a file to the server"""
    try:
        with open(file_path, 'rb') as f:
            files = {'file': (file_path, f)}
            res = requests.post(f"{BASE_URL}/upload", files=files)
        return res.json()
    except FileNotFoundError:
        return {"error": f"File '{file_path}' not found."}
    except Exception as e:
        return {"error": str(e)}

# def download_file(file_name):
#     """Download a file from the server"""
#     try:
#         res = requests.get(f"{BASE_URL}/download/{file_name}", stream=True)
#         if res.status_code == 200:
#             save_path = f"downloads/{file_name}"  # or use os.path.join
#             with open(save_path, 'wb') as f:
#                 for chunk in res.iter_content(chunk_size=8192):
#                     f.write(chunk)
#             return {"message": f"Downloaded '{file_name}' successfully."}
#         else:
#             return {"error": res.text}
#     except Exception as e:
#         return {"error": str(e)}
def download_file(file_name, save_path=None):
    """Download a file from the server and save it to the specified path (optional)"""
    try:
        res = requests.get(f"{BASE_URL}/download/{file_name}", stream=True)
        if res.status_code == 200:
            # Determine the full save path
            if save_path:
                # Ensure directory exists
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                full_path = save_path
            else:
                full_path = file_name  # Save to current directory

            # Write the file content
            with open(full_path, 'wb') as f:
                for chunk in res.iter_content(chunk_size=8192):
                    f.write(chunk)

            return {"message": f"Downloaded '{file_name}' to '{full_path}' successfully."}
        else:
            return {"error": res.text}
    except Exception as e:
        return {"error": str(e)}

def list_files():
    """List all files on the server"""
    try:
        res = requests.get(f"{BASE_URL}/list")
        return res.json()
    except Exception as e:
        return {"error": str(e)}

def delete_file(file_name):
    """Delete a file from the server"""
    try:
        res = requests.delete(f"{BASE_URL}/delete/{file_name}")
        return res.json()
    except Exception as e:
        return {"error": str(e)}
