from fastapi import Depends, FastAPI, HTTPException, Path, Request
from app.models import Recipe, StoredRecipe
from app.repository import RecipeRepository
from bson import ObjectId
from bson.errors import InvalidId

# Importações SlowAPI
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app = FastAPI(title="Recipes API")

app.state.limiter = limiter

app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


def recipe_object_id(
    recipe_id: str = Path(description="The ID of the recipe"),
):
    try:
        return ObjectId(recipe_id)
    except InvalidId:
        raise HTTPException(status_code=422, detail="Recipe id not valid")


@app.get("/", response_model=list[StoredRecipe])
@limiter.limit("5/minute")
def list_recipes(request: Request):
    return RecipeRepository.find_all()


@app.get("/{recipe_id}", response_model=StoredRecipe)
def get_recipe(recipe_oid: ObjectId = Depends(recipe_object_id)):
    result = RecipeRepository.find_by_id(recipe_oid)
    if result is None:
        raise HTTPException(status_code=404, detail="Recipe not found")

    return result


@app.post("/", response_model=StoredRecipe, status_code=201)
def create_recipe(recipe: Recipe):
    return RecipeRepository.insert(recipe)


@app.put("/{recipe_id}", response_model=StoredRecipe)
def update_recipe(
    new_recipe: Recipe,
    recipe_oid: ObjectId = Depends(recipe_object_id),
):
    return RecipeRepository.update(recipe_oid, new_recipe)


@app.delete("/{recipe_id}", status_code=204)
def delete_recipe(recipe_oid: ObjectId = Depends(recipe_object_id)):
    RecipeRepository.delete(recipe_oid)
