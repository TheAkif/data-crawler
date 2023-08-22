![Tests status](https://github.com/lorenzocesconetto/fastapi-postgresql/actions/workflows/actions.yml/badge.svg)

# FastAPI and PostgreSQL - Base Project Generator

This repo creates a basic FastAPI backend using cookiecutter.

## Why?

I've based my work on Tiangolo's [cookiecutter project](https://github.com/tiangolo/full-stack-fastapi-postgresql) project generator. But Tiangolo's project seems to be unmaintained for two years now. There's some code that I've ported from his project that still looks the same. Despite that, I've made some major changes.

I decided to create my own boilerplate in order to address some issues:
- Create a very simple and intuitive codebase.
- Update python and the packages to the latest version.
- Make some design changes that provide higher cohesion and lower coupling.

## Usage

Navigate with your terminal to the path where you'd like to create the new project.
Then run cookiecutter:
```
pip install cookiecutter
cookiecutter https://bitbucket.org/folio3/cookiecutter-fastapi/
```

## Setup (Temporary)

### Install Cookiecutter
```bash
pip install cookiecutter
```
### Apply Cookiecutter
```
cookiecutter <path where cloned>
```
## Create Virtual Environment
```bash
cd <project_directory> 
pipenv install 
pipenv shell
```
### Temporary changes
Navigate to app/core/config
Change(according to your db credentials):
```
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:<password>@<server>:<port>/<dbname>"
```
Navigate to migrations/eny.py
```
def get_url():
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "postgres")
    server = os.getenv("POSTGRES_SERVER", "db")
    db = os.getenv("POSTGRES_DB", "app")
    return "postgresql://postgres:<password>@<server>:<port>/<dbname>"
```
Comment these lines , and modify the return statement with your DATABASE_URI
```
def get_url():
    #user = os.getenv("POSTGRES_USER", "postgres")
    #password = os.getenv("POSTGRES_PASSWORD", "postgres")
    #server = os.getenv("POSTGRES_SERVER", "db")
    #db = os.getenv("POSTGRES_DB", "app")
    return "postgresql://postgres:<password>@<server>:<port>/<dbname>" # this will be your local database url
```

## Setting up databases

- Create a database of your choice, set username and password for postgres.
- Modify SQLALCHEMY_DATABASE_URI in .env file with your username, password, server (localhost), port(5432) and database name(fastapi) 
that you configured in the previous step as:
```bash
postgresql://<USERNAME>:<PASSWORD>@<SERVER>:<PORT>/<DB_NAME>
```

- Create another database for testing purposes.
- Modify SQLALCHEMY_TEST_DATABASE_URI in .env with the test database name. Other properties like username, password would be same as step 2.
```bash
postgresql://<USERNAME>:<PASSWORD>@<SERVER>:<PORT>/<TEST_DB_NAME>
```

## Starting the Server
```bash
uvicorn app.main:app --port 8080 --reload
```


## Testing

- As we have already created test database so we do not need to create the database again.
- Run the following command to run all the test cases:
```bash
pytest
```
- Run the following command to run test cases for one module i.e, 'items':
```bash
pytest tests/api/api_v1/test_items.py
```
- Run the following command to run specific test case like 'create an item':
```bash
pytest tests/api/api_v1/test_items.py::test_create_item
```

