import os
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from dotenv import load_dotenv

load_dotenv()

def get_engine() -> Engine:
    url = os.getenv("DATABASE_URL")
    return create_engine(url, pool_pre_ping=True, future=True)

def run_sql(sql: str, params: dict | None = None):
    engine = get_engine()
    with engine.connect() as conn:
        result = conn.execute(text(sql), params or {})
        try:
            return result.mappings().all()
        except Exception:
            return []
