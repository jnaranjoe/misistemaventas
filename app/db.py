import os
import psycopg
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://jnaranjo:Foxhound2912@localhost:5432/mi_base_datos"
)

def get_connection():
    return psycopg.connect(DATABASE_URL)