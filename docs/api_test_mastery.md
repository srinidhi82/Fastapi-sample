# API Test Automation Mastery — Learning Path

This guide will help you master API test automation using this repository as a playground.

## Goals
- Understand how to write reliable API tests with pytest and TestClient.
- Learn test design patterns: isolation, parametrization, fixtures, mocking, and edge-case testing.
- Learn how to integrate tests in CI and measure test coverage.

## Curriculum (hands-on tasks)
1. Run the tests and inspect results
   - `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`
   - `pytest -q`

2. Test basics
   - Read `tests/test_api.py` to see simple endpoint tests and a fixture that clears state between tests.
   - Add a test that asserts the OpenAPI schema exists (GET `/openapi.json`).

3. Parametrized tests & boundary checks
   - Open `tests/test_advanced.py` (added) to see `@pytest.mark.parametrize` examples.
   - Add param tests for invalid payloads (missing required fields, wrong types).

4. Mocking/Isolation
   - Learn `monkeypatch` (see `tests/test_advanced.py`) to replace functions and simulate external dependencies without network calls.
   - Add a test that simulates a DB failure and asserts the API returns a 5xx or appropriate error.

5. Test-driven additions
   - Follow TDD: write a failing test for a new feature (e.g., pagination for `GET /items`), implement the feature, re-run tests until passing.

6. Test maintenance & readability
   - Use descriptive test names, small test functions, and fixtures for setup/teardown.
   - Add comments in tests to explain the intent (not implementation details).

7. CI & coverage
   - Add a GitHub Actions workflow to run `pytest` on push/pull requests (I can add this for you).
   - Use `pytest --cov=app` to measure coverage and guard against regressions.

## Recommended exercises
- Add schema validation tests (assert 422 responses for invalid bodies).
- Add a test that ensures the example responses match the model schema.
- Add property-based tests with `hypothesis` for the `id_generator`.

---

## Reference: Useful pytest patterns
- Fixtures (scoped function/module/session)
- Parametrize (`@pytest.mark.parametrize("x,y", [(1,2),(3,4)])`)
- Monkeypatch (`monkeypatch.setattr(module, 'function', fake)`) to control behavior

---

If you'd like, I can add a GitHub Actions workflow to run `pytest` + coverage and add badges to `README.md`. Let me know and I'll add them.