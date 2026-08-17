from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import func

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.core.database import Base


class Cart(Base):

    __tablename__ = "carrito"

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

    estado: Mapped[str] = mapped_column(
        Enum("ACTIVO", "FINALIZADO")
    )

    detalles = relationship(
        "CartItem",
        back_populates="carrito"
    )
