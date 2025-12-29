import pytest
from app.utils import id_generator, SimpleData
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_id_generator_sequence():
    gen = id_generator(5)
    assert next(gen) == 5
    assert next(gen) == 6
    assert next(gen) == 7


@pytest.mark.parametrize("start,expected", [(1, 1), (10, 10), (99, 99)])
def test_id_generator_parametrized(start, expected):
    gen = id_generator(start)
    assert next(gen) == expected


def test_simpledataclass_to_dict():
    d = SimpleData(id=1, name="a")
    assert d.to_dict() == {"id": 1, "name": "a"}


def test_openapi_schema_exists():
    r = client.get("/openapi.json")
    assert r.status_code == 200
    assert "paths" in r.json()


def test_validation_error_for_missing_required_field():
    # missing 'name' should cause 422 Unprocessable Entity
    bad = {"id": 2}
    r = client.post("/items", json=bad)
    assert r.status_code == 422


def test_monkeypatch_example(monkeypatch):
    # Demonstrate monkeypatching a function used by the app (we patch fake_db access)
    from app import main

    # Replace the fake_db lookup to raise an exception to simulate a failing dependency
    def fake_get(_id):
        raise RuntimeError("DB failure")

    monkeypatch.setitem(main.__dict__, "fake_db", {})

    # Monkeypatch the get to raise
    monkeypatch.setitem(main.fake_db, 1, None)

    # Ensure the normal flow still returns 404 when not present
    r = client.get("/items/12345")
    assert r.status_code == 404

    # Optionally show how to monkeypatch a function; in a more complex app you would patch DB client functions
    # monkeypatch.setattr(target_module, 'remote_call', lambda *args, **kwargs: {'ok': True})
