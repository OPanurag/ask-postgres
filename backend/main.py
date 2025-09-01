from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os

app = FastAPI()

# Database URL
DATABASE_URL = os.getenv("DATABASE_URL")

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
