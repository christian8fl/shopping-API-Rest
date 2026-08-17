from fastapi import APIRouter
from sqlalchemy import text

from app.core.database import SessionLocal

router = APIRouter()

@router.get("/test-db")
def test_database():
    db = SessionLocal()
    try:
        db.execute(text("SELECT 1"))
        return {
            "message": "Conexión correcta con MySQL"
        }
    finally:

        db.close()
