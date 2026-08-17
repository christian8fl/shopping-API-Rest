from pydantic import BaseModel
from pydantic import ConfigDict


class CartItemCreate(BaseModel):

    producto_id: int
    cantidad: int


class CartItemResponse(BaseModel):

    id: int
    producto_id: int
    cantidad: int
    precio: float
    subtotal: float

    model_config = ConfigDict(
        from_attributes=True
    )


class CartResponse(BaseModel):

    id: int
    usuario_id: int
    estado: str

    model_config = ConfigDict(
        from_attributes=True
    )
