from pydantic import BaseModel
from pydantic import ConfigDict


class ProductCreate(BaseModel):

    categoria_id: int
    nombre: str
    descripcion: str | None = None
    precio: float
    stock: int
    imagen: str | None = None


class ProductUpdate(BaseModel):

    categoria_id: int
    nombre: str
    descripcion: str | None = None
    precio: float
    stock: int
    imagen: str | None = None
    activo: bool


class ProductResponse(BaseModel):

    id: int
    categoria_id: int
    nombre: str
    descripcion: str | None
    precio: float
    stock: int
    imagen: str | None
    activo: bool

    model_config = ConfigDict(
        from_attributes=True
    )
