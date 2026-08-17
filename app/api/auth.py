from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.repositories.user_repository import UserRepository

from app.schemas.auth import LoginRequest
from app.schemas.auth import Token

from app.services.auth_service import AuthService

router = APIRouter(

    prefix="/auth",

    tags=["Autenticación"]

)


@router.post(

    "/login",

    response_model=Token

)

def login(

    data: LoginRequest,

    db: Session = Depends(get_db)

):

    try:

        repository = UserRepository(db)

        service = AuthService(repository)

        return service.login(
            data.email,
            data.password
        )

    except Exception as e:

        raise HTTPException(
            status_code=401,
            detail=str(e)
        )
