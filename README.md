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

## What each file does 🔧

- `app/main.py` — FastAPI application with endpoints:
  - `GET /` — health check
  - `GET /items` — list all items
  - `GET /items/{item_id}` — fetch an item by id
  - `POST /items` — create a new item
  - `PUT /items/{item_id}` — update an existing item (path id must match JSON body id)
  - `DELETE /items/{item_id}` — delete an item

- `app/schemas.py` — Pydantic `Item` model and schema examples used by FastAPI in the OpenAPI docs

- `tests/test_api.py` — pytest tests for the API (covers create, duplicate, missing, list, update, delete)

- `requirements.txt` — project dependencies

- `README.md` — this file (how to run, examples, and explanation)

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
