# feedback-app

## Setup

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Set up the database:

    ```bash
    alembic upgrade head
    ```

3. Run the FastAPI server:

    ```bash
    uvicorn app.main:app --reload
    ```

4. Open `frontend/index.html` in your browser.

## API Documentation Swagger

The API documentation is available at [http://localhost:8000/docs](http://localhost:8000/docs).

## Tests

To run the tests, make sure you have a local Postgres instance running and a test database created. Then, run:

```bash
pytest
