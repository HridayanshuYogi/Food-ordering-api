from pydantic import BaseModel, ConfigDict


class FoodCreate(BaseModel):
    name: str
    description: str | None = None
    price: float


class FoodResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float

    model_config = ConfigDict(from_attributes=True)