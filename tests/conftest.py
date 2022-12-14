import os

from pytest import fixture
from fastapi.testclient import TestClient

from todo.app import app
from todo.cli import create_user, delete_user

# os.environ["TODO_DB__uri"] = "postgresql://postgres:postgres@db:5432/todo_test"

@fixture(scope='session')
def client():
    '''Test Client'''
    return TestClient(app)

def create_authenticated_user(username):
    '''Create a authenticated user given a username'''
    try:
        create_user(username, username)
    except Exception:
        print('Problema ao criar usuário')
        pass

    client = TestClient(app)

    token = client.post(
        "/token",
        data={"username": username, "password": username}
        # headers={"Content-Type": "application/x-www-form-urlencoded"},
    ).json()["access_token"]
    client.headers["Authorization"] = f"Bearer {token}"
    return client

@fixture(scope='function')
def authenticated_client():
    '''Create a authenticated user and delete at end of session'''
    yield create_authenticated_user(username='test_user')
    delete_user('test_user')
    
    
    