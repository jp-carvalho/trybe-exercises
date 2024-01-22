from fastapi.testclient import TestClient
from app.main import app
import pytest


@pytest.fixture
def client():
    return TestClient(app)


# limpar nossa db
@pytest.fixture(autouse=True)
def clear_db(monkeypatch):
    monkeypatch.setattr("app.main.RECIPES", [])


def test_list_recipes(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == []


def test_get_single_recipe(client, monkeypatch):
    mock_recipe = {
        "id": 1,
        "name": "Test Recipe",
        "ingredients": ["Test Ingredient 1", "Test Ingredient 2"],
        "instructions": "Test Instruction",
        "preparation_time": 10,
    }
    monkeypatch.setattr("app.main.RECIPES", [mock_recipe])
    response = client.get("/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, **mock_recipe}


def test_get_recipe_not_found(client):
    response = client.get("/10")
    assert response.status_code == 404
    assert response.json() == {"detail": "Recipe not found"}


def test_create_recipe(client):
    mock_recipe = {
        "name": "Test Recipe",
        "ingredients": ["Test Ingredient 1", "Test Ingredient 2"],
        "instructions": "Test Instruction",
        "preparation_time": 10,
    }
    response = client.post("/", json=mock_recipe)
    assert response.status_code == 201
    assert response.json() == {"id": 1, **mock_recipe}


def test_update_recipe(client, monkeypatch):
    mock_recipe = {
        "id": 1,
        "name": "Test Recipe",
        "ingredients": ["Test Ingredient 1", "Test Ingredient 2"],
        "instructions": "Test Instruction",
        "preparation_time": 10,
    }
    monkeypatch.setattr("app.main.RECIPES", [mock_recipe])

    new_recipe = {
        "name": "New Test Recipe",
        "ingredients": ["New Test Ingredient 1", "New Test Ingredient 2"],
        "instructions": "New Test Instruction",
        "preparation_time": 20,
    }

    response = client.put("/1", json=new_recipe)
    assert response.status_code == 200
    assert response.json() == {"id": 1, **new_recipe}


def test_delete_recipe(client, monkeypatch):
    mock_recipe = {
        "id": 1,
        "name": "Test Recipe",
        "ingredients": ["Test Ingredient 1", "Test Ingredient 2"],
        "instructions": "Test Instruction",
        "preparation_time": 10,
    }
    monkeypatch.setattr("app.main.RECIPES", [mock_recipe])

    response = client.delete("/1")
    assert response.status_code == 204
