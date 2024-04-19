from pydantic import BaseModel, Field, AliasChoices
from pydantic_mongo import ObjectIdField
from bson import ObjectId


class BaseDocument(BaseModel):
    id: ObjectIdField = Field(None, description="Object's ID", validation_alias=AliasChoices("_id", "id"))

    @property
    def _id(self) -> ObjectId:
        return self.id

    @property
    def cache_dict(self) -> dict:
        data = self.model_dump(mode='json')
        data["_id"] = str(data["id"])
        return data
