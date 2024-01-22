from app.main import app
from app.models import Recipe
from app.repository import RecipeRepository
from fastapi.testclient import TestClient
import pytest


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def clear_db():
    RecipeRepository._collection.drop()


def test_list_recipes(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == []


def test_get_single_recipe(client, monkeypatch):
    inserted = RecipeRepository.insert(
        Recipe(
            name="Test Recipe",
            ingredients=["Test Ingredient 1", "Test Ingredient 2"],
            instructions="Test Instruction",
            preparation_time=10,
        )
    )
    response = client.get(f"/{inserted.id}")
    assert response.status_code == 200
    assert response.json() == inserted.model_dump()


def test_get_recipe_not_found(client):
    response = client.get("/659f25c43e222ab886ffca02")
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
    assert response.json()["name"] == mock_recipe["name"]
    assert response.json()["ingredients"] == mock_recipe["ingredients"]
    assert response.json()["instructions"] == mock_recipe["instructions"]
    assert response.json()["preparation_time"] == mock_recipe["preparation_time"]

    assert response.json()["id"] is not None


def test_update_recipe(client):
    inserted = RecipeRepository.insert(
        Recipe(
            name="Test Recipe",
            ingredients=["Test Ingredient 1", "Test Ingredient 2"],
            instructions="Test Instruction",
            preparation_time=10,
        )
    )

    new_recipe = {
        "name": "New Test Recipe",
        "ingredients": ["New Test Ingredient 1", "New Test Ingredient 2"],
        "instructions": "New Test Instruction",
        "preparation_time": 20,
    }

    response = client.put(f"/{inserted.id}", json=new_recipe)
    assert response.status_code == 200
    assert response.json()["name"] == new_recipe["name"]
    assert response.json()["ingredients"] == new_recipe["ingredients"]
    assert response.json()["instructions"] == new_recipe["instructions"]
    assert response.json()["preparation_time"] == new_recipe["preparation_time"]


def test_delete_recipe(client):
    inserted = RecipeRepository.insert(
        Recipe(
            name="Test Recipe",
            ingredients=["Test Ingredient 1", "Test Ingredient 2"],
            instructions="Test Instruction",
            preparation_time=10,
        )
    )

    response = client.delete(f"/{inserted.id}")
    assert response.status_code == 204

    assert RecipeRepository.find_by_id(inserted.id) is None
