from fastapi import FastAPI, HTTPException, status
from app.schemas import ProductCreate, ProductUpdate, ProductOut
from app import crud

app = FastAPI(title="MiSistemaVentas API", version="1.1.0")

@app.get("/products", response_model=list[ProductOut])
def get_products():
    return crud.list_products()

@app.post("/products", response_model=ProductOut)
def post_product(payload: ProductCreate):
    return crud.create_product(payload.name, payload.price, payload.discount_percent)

@app.put("/products/{product_id}", response_model=ProductOut)
def put_product(product_id: int, payload: ProductUpdate):
    updated_product = crud.update_product(
        product_id, payload.name, payload.price, payload.discount_percent
    )
    if not updated_product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return updated_product

@app.get("/")
def root():
    return {"message": "API OK. Ve a /docs o /products"}