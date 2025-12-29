# Sample API (FastAPI)

A minimal FastAPI sample demonstrating CRUD endpoints (GET, POST, PUT, DELETE), request/response examples, and tests.

## Quick start 🚀

1. Create and activate a virtual environment (recommended):

   python3 -m venv .venv
   source .venv/bin/activate

2. Install dependencies:

   pip install -r requirements.txt

3. Run the app (local dev server):

   uvicorn app.main:app --reload --port 8000

   - Open the interactive docs at: http://127.0.0.1:8000/docs (Swagger UI)
   - Open the OpenAPI JSON at: http://127.0.0.1:8000/openapi.json

4. Run tests:

   pytest -q

---

## Learning resources included in this repo 📚

- `docs/api_test_mastery.md` — a hands-on learning path to master API test automation (fixtures, parametrization, mocking, CI integration).
- `docs/python_concepts.md` — focused explanations of Python concepts used in the project (classes, constructors, decorators, generators, dataclasses, `__main__`).
- `docs/file_logic_and_learning.md` — file-by-file logic and learning takeaways (per-file explanations).
- `tests/test_advanced.py` — additional tests demonstrating parametrization, generator tests, dataclass usage, monkeypatch example, and OpenAPI schema test.

Check those docs to follow a step-by-step plan to master API test development.
---

## What each Python file does 🔧

- `app/main.py` — FastAPI application and request handlers
  - Purpose: Define the API routes and implement request handling logic for a small CRUD service.
  - Key parts & logic:
    - `app = FastAPI(...)` — creates FastAPI app instance used by Uvicorn and test client.
    - `fake_db = {}` — an in-memory dictionary that stores `Item` instances by `id` (used only for examples/tests).
    - Route handlers (`@app.get`, `@app.post`, `@app.put`, `@app.delete`):
      - Validate input (FastAPI + Pydantic do this automatically for the `Item` body).
      - For `GET /items` return `list(fake_db.values())`.
      - For `GET /items/{item_id}` look up `fake_db[item_id]` and return a 404 if missing.
      - For `POST /items` check for duplicates then store the `Item` in `fake_db` and return 201.
      - For `PUT /items/{item_id}` ensure the path `item_id` exists and matches the body `id` then overwrite.
      - For `DELETE /items/{item_id}` remove the key from `fake_db` and return 204 (no content).
    - Errors: raise `HTTPException(status_code, detail)` for 4xx responses.
  - Learning outcomes:
    - How to define routes and use HTTP methods in FastAPI.
    - How FastAPI integrates with Pydantic for validation and OpenAPI generation.
    - How to return proper HTTP status codes and use `HTTPException`.

- `app/schemas.py` — Pydantic models and schema metadata
  - Purpose: Define the `Item` model used as request and response schema.
  - Key parts & logic:
    - `Item` inherits from `BaseModel` and uses `Field(..., json_schema_extra={"example": ...})` and `model_config` to provide examples.
    - Optional fields are typed with `Optional[...]` so FastAPI/Pydantic handle missing values.
  - Learning outcomes:
    - Basic Pydantic v2 model patterns (`BaseModel`, `Field`, `ConfigDict`/`model_config`).
    - Adding JSON schema examples so OpenAPI/Swagger UI shows sample payloads.

- `tests/test_api.py` — test suite using pytest and FastAPI TestClient
  - Purpose: Validate the API behavior (happy paths and error cases).
  - Key parts & logic:
    - `TestClient(app)` to call endpoints without starting a server.
    - `pytest.fixture(autouse=True)` used to clear `fake_db` between tests to ensure isolation.
    - Tests cover: root health check, create/get, create-duplicate (400), get-missing (404), list, update, delete.
  - Learning outcomes:
    - How to write API tests with pytest and TestClient.
    - Using fixtures to set up/tear down shared state.
    - Asserting HTTP status codes and JSON payloads.

- `requirements.txt` — project dependencies
  - Purpose: Pin libraries required to run and test the project (FastAPI, Uvicorn, pytest, httpx dependency for TestClient).
  - Learning outcomes:
    - How to manage dependencies for a Python project.

- `.gitignore` — local/venv and OS ignored files
  - Purpose: Prevent committing environment artifacts (like `.venv/`, caches) into git.

- `README.md` — documentation, usage and examples (this file)
  - Purpose: Explain how to set up, run, test, and understand the project.

- `tests/__init__.py` (if present) — makes `tests` a package for some test runners (not required here)


For a more in-depth per-file explanation, see `docs/file_logic_and_learning.md` (added to this repo).
---

## Request / Response examples (curl) 💡

Create an item (POST):

curl -s -X POST "http://127.0.0.1:8000/items" -H "Content-Type: application/json" -d '{"id":1,"name":"Sample","description":"A sample item"}'

Response (201):

{"id":1,"name":"Sample","description":"A sample item"}

List items (GET):

curl -s "http://127.0.0.1:8000/items"

Response (200):

[{"id":1,"name":"Sample","description":"A sample item"}]

Get item (GET):

curl -s "http://127.0.0.1:8000/items/1"

Response (200):

{"id":1,"name":"Sample","description":"A sample item"}

Update item (PUT):

curl -s -X PUT "http://127.0.0.1:8000/items/1" -H "Content-Type: application/json" -d '{"id":1,"name":"Updated","description":"Updated"}'

Response (200):

{"id":1,"name":"Updated","description":"Updated"}

Delete item (DELETE):

curl -s -X DELETE "http://127.0.0.1:8000/items/1"

Response (204): (no body)

---

## Notes & next steps ✨

- FastAPI auto-generates interactive API docs (`/docs`) and OpenAPI schema (`/openapi.json`).
- To add persistence, replace the in-memory `fake_db` with a database (SQLite, PostgreSQL) using an ORM like SQLModel or SQLAlchemy.
- Want me to add a `list` endpoint with pagination, or integrate SQLite persistence? Tell me which and I'll add it.
