from sqlalchemy import Boolean
from sqlalchemy import DECIMAL
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.core.database import Base


class Product(Base):

    __tablename__ = "productos"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    categoria_id: Mapped[int] = mapped_column(
        ForeignKey("categorias.id")
    )

    nombre: Mapped[str] = mapped_column(
        String(150)
    )

    descripcion: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    precio: Mapped[float] = mapped_column(
        DECIMAL(10, 2)
    )

    stock: Mapped[int] = mapped_column(
        Integer
    )

    imagen: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    activo: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    categoria = relationship(
        "Category",
        back_populates="productos"
    )
