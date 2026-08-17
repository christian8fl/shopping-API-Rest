from fastapi import FastAPI

from app.api.test_db import router as test_router
from app.api.users import router as user_router
from app.api.auth import router as auth_router
from app.api.categories import router as category_router
from app.api.products import router as product_router

app = FastAPI(
    title="Shopping API",
    version="1.0.0"
)

app.include_router(test_router)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(category_router)
app.include_router(product_router)

@app.get("/")
def home():
    return {
        "message": "Shopping API funcionando correctamente"
    }

@app.get("/sumar")
def sumar(a: float, b: float):
    return {
        "numero1": a,
        "numero2": b,
        "resultado": a + b
    }