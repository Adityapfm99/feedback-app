# feedback-app

## Setup

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Created the migration script:

    ```bash
    alembic revision --autogenerate -m "Initial migration"
    ```

3. Apply the New Migration:

    ```bash
   alembic upgrade head
    ```



4. Run the FastAPI server (backend):

    ```bash
    uvicorn app.main:app --reload
    ```

5. Run the FastAPI server (Frontend):

    ```bash
   npm run serve
    ```

## API Documentation Swagger

The API documentation is available at [http://localhost:8000/docs](http://localhost:8000/docs).

## Tests

To run the tests, make sure you have a local Postgres instance running and a test database created. Then, run:

```bash
pytest
