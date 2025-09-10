from app.main import read_root

def test_read_root():
    assert read_root() == {"message": "Hello from FastAPI on Azure ACR!"}
