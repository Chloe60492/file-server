from app.config import FILE_SERVER_URL
import uuid
from app.tests.utils import generate_filename, create_temp_file, session 


# --- DELETE TESTS ---
def test_delete_nonexistent_file(session):
    r = session.delete(f"{FILE_SERVER_URL}/delete/notfound_{uuid.uuid4().hex}.txt")
    assert r.status_code == 404

def test_delete_twice(session):
    filename = generate_filename("del")
    path = create_temp_file(filename, 5)
    with open(path, 'rb') as f:
        files = {'file': (filename, f)}
        session.post(f"{FILE_SERVER_URL}/upload", files=files)
    path.unlink()

    r1 = session.delete(f"{FILE_SERVER_URL}/delete/{filename}")
    r2 = session.delete(f"{FILE_SERVER_URL}/delete/{filename}")

    assert r1.status_code == 200
    assert r2.status_code == 404

