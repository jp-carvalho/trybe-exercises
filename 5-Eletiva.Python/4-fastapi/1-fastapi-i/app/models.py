from pydantic import BaseModel, Field


class Recipe(BaseModel):
    name: str = Field(description="Nome da receita", max_length=100)
    ingredients: list[str]
    instructions: str
    preparation_time: int


class StoredRecipe(Recipe):
    id: str
