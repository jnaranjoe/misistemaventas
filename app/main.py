from fastapi import FastAPI
from app.schemas import ProductCreate, ProductOut
from app import crud

app = FastAPI(title="MiSistemaVentas API", version="1.1.0")

@app.get("/products", response_model=list[ProductOut])
def get_products():
    return crud.list_products()

@app.post("/products", response_model=ProductOut)
def post_product(payload: ProductCreate):
    return crud.create_product(payload.name, payload.price, payload.discount_percent)

@app.get("/")
def root():
    return {"message": "API OK. Ve a /docs o /products"}