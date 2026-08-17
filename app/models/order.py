from sqlalchemy import DECIMAL
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import func

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.core.database import Base


class Order(Base):

    __tablename__ = "pedidos"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    usuario_id: Mapped[int] = mapped_column(
        ForeignKey("usuarios.id")
    )

    fecha: Mapped[DateTime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    total: Mapped[float] = mapped_column(
        DECIMAL(10, 2)
    )

    detalles = relationship(
        "OrderItem",
        back_populates="pedido"
    )
