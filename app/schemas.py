from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    price: float = Field(gt=0)

class ProductOut(BaseModel):
    id: int
    name: str
    price: float