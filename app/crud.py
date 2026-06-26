from app.db import get_connection

def create_product(name: str, price: float, discount_percent: float = 0) -> dict:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO product(name, price, discount_percent) VALUES (%s, %s, %s) RETURNING id, name, price, discount_percent",
                (name, price, discount_percent)
            )
            row = cur.fetchone()
            conn.commit()
            return {
                "id": row[0],
                "name": row[1],
                "price": float(row[2]),
                "discount_percent": float(row[3])
            }

def list_products() -> list[dict]:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name, price, discount_percent FROM product ORDER BY id")
            rows = cur.fetchall()
            return [
                {"id": r[0], "name": r[1], "price": float(r[2]), "discount_percent": float(r[3])}
                for r in rows
            ]
        
def update_product(product_id: int, name: str | None, price: float | None, discount_percent: float | None) -> dict | None:
    with get_connection() as conn:
        with conn.cursor() as cur:
            # Primero verificamos si el producto existe
            cur.execute("SELECT name, price, discount_percent FROM product WHERE id = %s", (product_id,))
            current_data = cur.fetchone()
            if not current_data:
                return None
            
            # Si un campo viene como None, mantenemos el valor actual en la BD
            final_name = name if name is not None else current_data[0]
            final_price = price if price is not None else current_data[1]
            final_discount = discount_percent if discount_percent is not None else current_data[2]
            
            cur.execute(
                "UPDATE product SET name = %s, price = %s, discount_percent = %s WHERE id = %s RETURNING id, name, price, discount_percent",
                (final_name, final_price, final_discount, product_id)
            )
            row = cur.fetchone()
            conn.commit()
            return {
                "id": row[0],
                "name": row[1],
                "price": float(row[2]),
                "discount_percent": float(row[3])
            }
        
def delete_product(product_id: int) -> bool:
    with get_connection() as conn:
        with conn.cursor() as cur:
            # Verificamos si existe antes de borrar
            cur.execute("SELECT id FROM product WHERE id = %s", (product_id,))
            if not cur.fetchone():
                return False
            
            cur.execute("DELETE FROM product WHERE id = %s", (product_id,))
            conn.commit()
            return True