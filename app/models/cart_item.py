from sqlalchemy import DECIMAL
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.core.database import Base


class CartItem(Base):

    __tablename__ = "carrito_detalle"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    carrito_id: Mapped[int] = mapped_column(
        ForeignKey("carrito.id")
    )

    producto_id: Mapped[int] = mapped_column(
        ForeignKey("productos.id")
    )

    cantidad: Mapped[int] = mapped_column(
        Integer
    )

    precio: Mapped[float] = mapped_column(
        DECIMAL(10, 2)
    )

    subtotal: Mapped[float] = mapped_column(
        DECIMAL(10, 2)
    )

    carrito = relationship(
        "Cart",
        back_populates="detalles"
    )
