from app.database import db
from app.models import Recipe, StoredRecipe
from bson import ObjectId


class RecipeRepository:
    """reposnsável por interagir com o banco"""

    _collection = db["recipes"]

    @classmethod
    def find_all(cls) -> list[StoredRecipe]:
        find_result = cls._collection.find({})

        result = []
        for recipe in find_result:
            id_str = str(recipe.pop("_id"))

            result.append(
                StoredRecipe(id=id_str, **recipe),
            )

        return result

    @classmethod
    def find_by_id(cls, id: str) -> StoredRecipe:
        find_result = cls._collection.find_one({"_id": ObjectId(id)})

        if find_result is None:
            return None

        id_str = str(find_result.pop("_id"))
        return StoredRecipe(id=id_str, **find_result)

    @classmethod
    def insert(cls, recipe: Recipe) -> StoredRecipe:
        insert_result = cls._collection.insert_one(recipe.model_dump())

        return cls.find_by_id(insert_result.inserted_id)

    @classmethod
    def update(cls, id: str, recipe: Recipe) -> StoredRecipe:
        update_result = cls._collection.find_one_and_update(
            {"_id": ObjectId(id)}, {"$set": recipe.model_dump()}
        )

        return cls.find_by_id(update_result["_id"])

    @classmethod
    def delete(cls, id: str):
        cls._collection.delete_one({"_id": ObjectId(id)})
