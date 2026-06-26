from pydantic import BaseModel, Field
from typing import Optional

class ProductCreate(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    price: float = Field(gt=0)
    discount_percent: float = Field(default=0, ge=0, le=100)

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=80)
    price: Optional[float] = Field(None, gt=0)
    discount_percent: Optional[float] = Field(None, ge=0, le=100)

class ProductOut(BaseModel):
    id: int
    name: str
    price: float
    discount_percent: float