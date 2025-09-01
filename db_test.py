import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Load env vars
load_dotenv()

db_url = os.getenv("DATABASE_URL")
if not db_url:
    raise ValueError("❌ No DATABASE_URL found in .env")

# Connect using SQLAlchemy
engine = create_engine(db_url)

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        version = result.scalar()
        print("✅ Connected to PostgreSQL!")
        print("Version:", version)
except Exception as e:
    print("❌ Database connection failed:", e)
