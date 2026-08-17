from sqlalchemy import DECIMAL
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.core.database import Base


class OrderItem(Base):

    __tablename__ = "pedido_detalle"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    pedido_id: Mapped[int] = mapped_column(
        ForeignKey("pedidos.id")
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

    pedido = relationship(
        "Order",
        back_populates="detalles"
    )
