# feedback-app

1. How to Start
    ```bash
    1. git clone https://github.com/Adityapfm99/feedback-app
    2. python -m venv env
    3. source env/bin/activate
    4. pip install -r requirements.txt
    5. Rename file .env_sample to .env

    ```
2. Migration Tools (Alembic)
   
    ```bash
    alembic init alembic
    alembic revision --autogenerate -m "Create feedback table"
    
    ```
     ![Alt text](/image/alembic.png)

    ```bash
    and migration script is generated
     ![Alt text](/image/migration_script.png.png)
    ```

     ```bash
        alembic upgrade head
    ```

3. Run the FastAPI server (backend):

    ```bash
    uvicorn app.main:app --reload
    ```
    ![Alt text](/image/startBe.png)


4. Run the FastAPI server (Frontend):

    ```bash
    npm run serve
    ```
    ![Alt text](/image/startfe.png.png)
    ![Alt text](/image/ui.png)

    ```bash
    succesfuly created
    ```

    ![Alt text](/image/submitted.png)

    ```bash
    result db
    ```
    ![Alt text](/image/result_db.png)

    ```bash
        
        curl --location 'http://localhost:8000/feedback/' \
            --header 'Content-Type: application/json' \
            --data '{
                "rating": 1
            }'
     ```
## API Documentation Swagger

5. The API documentation is available at [http://localhost:8000/docs](http://localhost:8000/docs)

    ![Alt text](/image/swagger.png)

## Unit Tests

6. To run the tests, make sure you have a local Postgres instance running and a test database created. Then, run:

    ```bash
    pytest
    ```

    ![Alt text](/image/unittest.png)
