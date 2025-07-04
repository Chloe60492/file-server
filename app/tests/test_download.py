from app.config import FILE_SERVER_URL
from app.tests.utils import generate_filename, create_temp_file, session 

# --- DOWNLOAD TESTS ---

def test_download_file_without_filename(session):
    r = session.get(f"{FILE_SERVER_URL}/download", params={"filename": ""})
    assert r.status_code == 400
    assert r.json()["detail"] == "Filename required."

def test_download_nonexistent_file(session):
    name = "not_exist_123.txt"
    r = session.get(f"{FILE_SERVER_URL}/download", params={"filename": name})
    assert r.status_code == 404

def test_download_case_sensitive(session):
    filename = generate_filename("case")
    path = create_temp_file(filename, 10)

    with open(path, 'rb') as f:
        files = {'file': (filename, f)}
        session.post(f"{FILE_SERVER_URL}/upload", files=files)

    wrong_case = filename.upper()
    r = session.get(f"{FILE_SERVER_URL}/download", params={"filename": wrong_case})
    assert r.status_code == 404
    path.unlink()