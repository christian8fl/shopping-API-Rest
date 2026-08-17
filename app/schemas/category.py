from pydantic import BaseModel
from pydantic import ConfigDict


class CategoryCreate(BaseModel):

    nombre: str
    descripcion: str | None = None


class CategoryUpdate(BaseModel):

    nombre: str
    descripcion: str | None = None
    activo: bool


class CategoryResponse(BaseModel):

    id: int
    nombre: str
    descripcion: str | None
    activo: bool

    model_config = ConfigDict(
        from_attributes=True
    )
