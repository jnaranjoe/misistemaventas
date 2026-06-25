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