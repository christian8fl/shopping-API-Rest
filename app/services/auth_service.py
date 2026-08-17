from app.core.security import create_access_token
from app.core.security import verify_password

from app.repositories.user_repository import UserRepository


class AuthService:

    def __init__(self, repository: UserRepository):

        self.repository = repository


    def login(self, email: str, password: str):

        user = self.repository.get_by_email(email)

        if user is None:
            raise Exception("Credenciales incorrectas.")

        if not verify_password(
            password,
            user.password
        ):
            raise Exception("Credenciales incorrectas.")

        token = create_access_token(

            {
                "sub": str(user.id),
                "email": user.email
            }

        )

        return {

            "access_token": token,

            "token_type": "bearer"

        }
