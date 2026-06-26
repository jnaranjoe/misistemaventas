from fastapi import FastAPI, HTTPException, status
from app.schemas import ProductCreate, ProductUpdate, ProductOut
from app import crud


app = FastAPI(title="MiSistemaVentas API", version="1.2.0")

@app.get("/")
def root():
    return {"message": "API OK. Ve a /docs para probar los endpoints CRUD"}

@app.get("/products", response_model=list[ProductOut])
def get_products():
    return crud.list_products()

@app.post("/products", response_model=ProductOut, status_code=status.HTTP_201_CREATED)
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

@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int):
    success = crud.delete_product(product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return None