from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    price: float = Field(gt=0)
    discount_percent: float = Field(default=0, ge=0, le=100) # Nueva validación

class ProductOut(BaseModel):
    id: int
    name: str
    price: float
    discount_percent: float