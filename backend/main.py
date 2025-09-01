from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

app = FastAPI()

# Load environment variables
load_dotenv()

# Get DB URL
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL not found. Check your .env file!")

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.get("/")
def root():
    return {"message": "Backend is running 🚀"}

@app.get("/employees")
def get_employees():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM employees"))
            return [dict(row._mapping) for row in result]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/departments")
def get_departments():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM departments"))
            return [dict(row._mapping) for row in result]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
