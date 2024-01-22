from fastapi import FastAPI, HTTPException
from app.models import Recipe, StoredRecipe
from app.repository import RecipeRepository

app = FastAPI(title="Recipes API")


@app.get("/", response_model=list[StoredRecipe])
def list_recipes():
    return RecipeRepository.find_all()


@app.get("/{recipe_id}", response_model=StoredRecipe)
def get_recipe(recipe_id: str):
    result = RecipeRepository.find_by_id(recipe_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Recipe not found")

    return result


@app.post("/", response_model=StoredRecipe, status_code=201)
def create_recipe(recipe: Recipe):
    return RecipeRepository.insert(recipe)


@app.put("/{recipe_id}", response_model=StoredRecipe)
def update_recipe(new_recipe: Recipe, recipe_id: str):
    return RecipeRepository.update(recipe_id, new_recipe)


@app.delete("/{recipe_id}", status_code=204)
def delete_recipe(recipe_id: str):
    RecipeRepository.delete(recipe_id)
