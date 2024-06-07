# feedback-app

## Setup
1. How to Start
    ```bash
    1. git clone https://github.com/Adityapfm99/feedback-app
    2. python -m venv env
    3. source env/bin/activate
    4. pip install -r requirements.txt
    5. Rename file env_sample to .env
    6. alembic revision --autogenerate -m "Create feedback table"
    7. alembic upgrade head
    ```


2. Run the FastAPI server (backend):

    ```bash
    uvicorn app.main:app --reload
    ```
3. Run the FastAPI server (Frontend):

    ```bash
    npm run serve
    ```
    ![Alt text](/image/ui.png)

## API Documentation Swagger

4. The API documentation is available at [http://localhost:8000/docs](http://localhost:8000/docs)

    ![Alt text](/image/swagger.png)

## Tests

5. To run the tests, make sure you have a local Postgres instance running and a test database created. Then, run:

```bash
pytest
 ```

![Alt text](/image/unittest.png)
