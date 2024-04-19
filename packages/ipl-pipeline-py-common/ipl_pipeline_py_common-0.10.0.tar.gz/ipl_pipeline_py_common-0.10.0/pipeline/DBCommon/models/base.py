from pydantic import BaseModel, Field
from pydantic_mongo import ObjectIdField
from bson import ObjectId


class BaseDocument(BaseModel):
    id: ObjectIdField = Field(None, alias="_id", description="Object's ID")

    @property
    def _id(self) -> ObjectId:
        return self.id

    @property
    def cache_dict(self) -> dict:
        data = self.model_dump(mode='json')
        data["_id"] = str(data["id"])
        return data
