from fastapi import FastAPI, HTTPException, Path

app = FastAPI(title="Recipes API")

RECIPES: list[dict] = []


# Listar todas
@app.get("/", response_model=list[dict])
def list_recipes():
    return RECIPES


# Listar uma
@app.get("/{recipe_id}", response_model=dict)
# define que o id deve ser maior que 0 (gt=0)
def get_recipe(recipe_id: int = Path(gt=0)):
    try:
        return RECIPES[recipe_id - 1]
    except IndexError:
        raise HTTPException(status_code=404, detail="Recipe not found")


# Criar
@app.post("/", response_model=dict, status_code=201)
def create_recipe(recipe: dict):
    recipe["id"] = len(RECIPES) + 1
    RECIPES.append(recipe)
    return recipe


# Atualizar
@app.put("/{recipe_id}", response_model=dict)
def update_recipe(new_recipe: dict, recipe_id: int = Path(gt=0)):
    RECIPES[recipe_id - 1].update(new_recipe)

    return RECIPES[recipe_id - 1]


# Deletar
@app.delete("/{recipe_id}", status_code=204)
def delete_recipe(recipe_id: int = Path(gt=0)):
    try:
        RECIPES.pop(recipe_id - 1)
    except IndexError:
        raise HTTPException(status_code=404, detail="Recipe not found")
