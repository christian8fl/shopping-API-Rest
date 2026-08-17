from pydantic import BaseModel
from pydantic import ConfigDict


class OrderItemResponse(BaseModel):

    producto_id: int
    cantidad: int
    precio: float
    subtotal: float

    model_config = ConfigDict(
        from_attributes=True
    )


class OrderResponse(BaseModel):

    id: int
    usuario_id: int
    total: float

    model_config = ConfigDict(
        from_attributes=True
    )
