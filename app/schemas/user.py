from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr


class UserCreate(BaseModel):

    nombres: str
    apellidos: str
    email: EmailStr
    password: str


class UserUpdate(BaseModel):

    nombres: str
    apellidos: str
    email: EmailStr
    activo: bool


class UserResponse(BaseModel):

    id: int
    nombres: str
    apellidos: str
    email: EmailStr
    activo: bool

    model_config = ConfigDict(
        from_attributes=True
    )
