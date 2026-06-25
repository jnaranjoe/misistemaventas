from app.db import get_connection

def create_product(name: str, price: float) -> dict:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO product(name, price) VALUES (%s, %s) RETURNING id, name, price",
                (name, price)
            )
            row = cur.fetchone()
            conn.commit()
            return {"id": row[0], "name": row[1], "price": float(row[2])}

def list_products() -> list[dict]:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name, price FROM product ORDER BY id")
            rows = cur.fetchall()
            return [{"id": r[0], "name": r[1], "price": float(r[2])} for r in rows]