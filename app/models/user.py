from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import func

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.database import Base

class User(Base):

    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    nombres: Mapped[str] = mapped_column(
        String(100)
    )

    apellidos: Mapped[str] = mapped_column(
        String(100)
    )

    email: Mapped[str] = mapped_column(
        String(150),
        unique=True
    )

    password: Mapped[str] = mapped_column(
        String(255)
    )

    activo: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    fecha_creacion: Mapped[DateTime] = mapped_column(
        DateTime,
        server_default=func.now()
    )
