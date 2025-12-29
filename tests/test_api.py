import pytest
from fastapi.testclient import TestClient
from app.main import app, fake_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def clear_db():
    # ensure clean state between tests
    fake_db.clear()
    yield


def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Sample API is running"}


def test_create_and_get_item():
    item = {"id": 1, "name": "Sample", "description": "A sample item"}
    r = client.post("/items", json=item)
    assert r.status_code == 201
    assert r.json() == item

    r2 = client.get("/items/1")
    assert r2.status_code == 200
    assert r2.json() == item


def test_create_duplicate_item():
    item = {"id": 1, "name": "Sample", "description": "A sample item"}
    r1 = client.post("/items", json=item)
    assert r1.status_code == 201
    r2 = client.post("/items", json=item)
    assert r2.status_code == 400


def test_get_missing_item():
    r = client.get("/items/999")
    assert r.status_code == 404


def test_create_item_content_type_header():
    item = {"id": 42, "name": "ContentTypeTest", "description": "Check header"}
    r = client.post("/items", json=item)
    assert r.status_code == 201
    # Ensure server sets Content-Type header for JSON responses
    assert r.headers.get("content-type", "").startswith("application/json")


def test_list_items():
    item1 = {"id": 1, "name": "One"}
    item2 = {"id": 2, "name": "Two"}
    client.post("/items", json=item1)
    client.post("/items", json=item2)
    r = client.get("/items")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
    assert len(r.json()) == 2


def test_update_item():
    item = {"id": 1, "name": "Sample", "description": "A sample item"}
    client.post("/items", json=item)
    updated = {"id": 1, "name": "Updated", "description": "Updated"}
    r = client.put("/items/1", json=updated)
    assert r.status_code == 200
    assert r.json() == updated


def test_delete_item():
    item = {"id": 1, "name": "Sample"}
    client.post("/items", json=item)
    r = client.delete("/items/1")
    assert r.status_code == 204
    r2 = client.get("/items/1")
    assert r2.status_code == 404
