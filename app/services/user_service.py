from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.core.security import hash_password

class UserService:

    def __init__(self, repository: UserRepository):

        self.repository = repository


    def create(self, data: UserCreate):

        user = self.repository.get_by_email(data.email)

        if user:

            raise Exception("El correo ya existe.")


        new_user = User(

            nombres=data.nombres,

            apellidos=data.apellidos,

            email=data.email,

            password=hash_password(data.password)

        )

        return self.repository.create(new_user)


    def get_all(self):

        return self.repository.get_all()
