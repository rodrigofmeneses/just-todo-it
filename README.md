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

(Imagem do docker Desktop aqui)

To run tests a simple file has created in `test.sh`, so just run it.

(Imagem dos testes)

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
