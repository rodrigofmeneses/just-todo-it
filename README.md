# Just TODO it API

![Just TODO it Gif](assets/just_todo_it.gif)

> This Project is a boilerplate for Python FastAPI projects. The idea implemented is to be container first, so as not to have the problem of "it runs on my machine". 
>
> For that there are `Dockerfile.dev` file to resolve the main dependencies of the project. And the `postgres/Dockerfile` file for the database dependencies.
---

**Technologies used:** 

The mainly technologies used are:
* Python
* FastAPI

For database model and migrations:
* SQLModel
* Alembic

Check it out `requirements.in` and `requirements-dev.txt` for the majors Python and FastAPI dependencies to development.

Last and not least
* Docker 
* PostgreSQL

---
**Configuration:**

This project is design to be container first, so after cloning the respository:

```
docker-compose up
```
In other terminal, execute to apply migrations:
```
docker-compose exec api alembic upgrade head
```

To run tests a simple file has created in `test.sh`, so just run it.

First type `chmod +x test.sh` to create a executable, so `./test.sh`:

```
[+] Running 2/2
 ⠿ Container todo-api-db-1   Running                                           0.0s
 ⠿ Container todo-api-api-1  Started                                           1.1s

=============================== test session starts ================================
platform linux -- Python 3.11.0, pytest-7.2.0, pluggy-1.0.0 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /home/app/api
plugins: anyio-3.6.2, order-1.0.1
collected 5 items                                                                  

tests/test_user.py::test_encode_password_hash PASSED                         [ 20%]
tests/test_user.py::test_verify_password_with_correctly_data PASSED          [ 40%]
tests/test_user.py::test_verify_password_with_wrong_data PASSED              [ 60%]
tests/test_user.py::test_two_passwords_has_different_hashs PASSED            [ 80%]
tests/test_user.py::test_user_password_is_hashed PASSED                      [100%]

=========================== 5 passed, 1 warning in 2.15s ===========================
[+] Running 3/3
 ⠿ Container todo-api-api-1  Removed                                           1.0s
 ⠿ Container todo-api-db-1   Removed                                           0.5s
 ⠿ Network todo-api_default  Removed                                           0.4s
```

If you opt for non docker developer environment, follow these steps:

1. Create a virtual environment and install all dependencies:

```
# Create virtual environment and activate
python -m venv .venv
source .venv/bin/activate # Linux
.venv/script/activate # Windows

# Install dependencies
pip install -r requirements-dev.txt
pip install -e . # Install the project to use CLI
```

2. Setup Database, copy `postgres/create-databases.sh` to `/docker-entrypoint-initdb.d/` folder in your system and restart your PostgreSQL to create a database in initalization. 

3. Configure environment variables in `todo/default.toml` or `.env` if prefer.

4. Run project:
```
uvicorn todo.app:app --host=0.0.0.0 --port=8000 --reload
```
---

**Usage**

Access `http://localhost:8000/docs` or `http://localhost:8000/redoc` to visualize the project documentation.

You can interact with swagger and test the routes.

<!-- If you want to test using a rest client, you can click the button below:

[![Run in Insomnia}](https://insomnia.rest/images/run.svg)]()

**Here's my project deployed to** -->
