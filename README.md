# GovTech
Gov Tech Assignment

# Running the application
1. Clone the repository
2. Update the configuration in the `dev.yaml` file (app/config/dev.yaml)
3. Run docker compose -f docker-compose.yaml up

# Running the without docker
1. Clone the repository
2. Update the configuration in the `dev.yaml` file (app/config/dev.yaml)
    - change host value to localhost
3. Run the following commands from the root directory
    - pip install -r requirements.txt
    - uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# Running the tests
Can use the given postman collection (gov_tech.postman_collection)