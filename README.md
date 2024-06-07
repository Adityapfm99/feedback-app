# feedback-app

## Setup
1. Clone Repository
    ```bash
    git clone https://github.com/Adityapfm99/feedback-app
    ```
2. Create & Activate virtual env
   ```bash
   python -m venv env
   source env/bin/activate

    ```
1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```
      ```bash
    pip install -r requirements.txt
    ```

2. Created the migration script:

    ```bash
    alembic revision --autogenerate -m "Create feedback table"
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
![Alt text](/image/ui.png)

## API Documentation Swagger

The API documentation is available at [http://localhost:8000/docs](http://localhost:8000/docs)

![Alt text](/image/swagger.png)

## Tests

To run the tests, make sure you have a local Postgres instance running and a test database created. Then, run:

```bash
pytest
 ```

![Alt text](/image/unittest.png)
