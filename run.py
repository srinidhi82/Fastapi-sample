"""Run helper for development.

This file provides a safe `__main__` entrypoint so you can run the app directly for
local development with `python run.py` without getting relative-import errors.

It uses `uvicorn.run` to start the FastAPI app defined in `app.main:app`.
"""

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
