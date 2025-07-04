import pytest
from pathlib import Path
from app.config import FILE_SERVER_URL
import os
from app.tests.utils import generate_filename, create_temp_file, session 

# --- UPLOAD TESTS ---
def test_upload_file_not_found(session):
    print("BASE_URL =", os.getenv("FILE_SERVER_URL"))
    path = "nonexistent.txt"
    with pytest.raises(FileNotFoundError):
        with open(path, 'rb') as f:
            pass

def test_upload_empty_file(session):
    filename = generate_filename("empty")
    path = create_temp_file(filename, 0)
    with open(path, 'rb') as f:
        files = {'file': (filename, f)}
        r = session.post(f"{FILE_SERVER_URL}/upload", files=files)
    print("Response:", r.status_code, r.text)
    assert r.status_code == 400
    assert r.json()["detail"] == "Empty file."
    path.unlink()

def test_upload_long_filename(session):
    long_name = "a" * 240 + ".txt"
    path = create_temp_file(long_name, 10)
    with open(path, 'rb') as f:
        files = {'file': (long_name, f)}
        r = session.post(f"{FILE_SERVER_URL}/upload", files=files)
    assert r.status_code in [200, 400, 414]  # 根據 server 處理方式
    path.unlink()

def test_upload_duplicate_file(session):
    filename = generate_filename("dup")
    path = create_temp_file(filename, 50)
    with open(path, 'rb') as f:
        files = {'file': (filename, f)}
        r1 = session.post(f"{FILE_SERVER_URL}/upload", files=files)
    with open(path, 'rb') as f:
        files = {'file': (filename, f)}
        r2 = session.post(f"{FILE_SERVER_URL}/upload", files=files)
    assert r1.status_code == 200
    assert r2.status_code in [200, 409]
    path.unlink()

# --- LIST TESTS ---
def test_list_files_normal(session):
    r = session.get(f"{FILE_SERVER_URL}/list")
    assert r.status_code == 200
    assert isinstance(r.json(), list)


