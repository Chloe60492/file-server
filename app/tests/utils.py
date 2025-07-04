import requests
import pytest
from pathlib import Path
from app.config import FILE_SERVER_URL
import uuid


def generate_filename(prefix="test", ext=".txt"):
    return f"{prefix}_{uuid.uuid4().hex[:6]}{ext}"

def create_temp_file(name, size=0):
    path = Path(name)
    with open(path, 'wb') as f:
        f.write(b'x' * size)
    return path

@pytest.fixture(scope="module")
def session():
    return requests.Session()