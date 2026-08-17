from app.models.category import Category

from app.repositories.category_repository import CategoryRepository

from app.schemas.category import CategoryCreate
from app.schemas.category import CategoryUpdate


class CategoryService:

    def __init__(self, repository: CategoryRepository):

        self.repository = repository


    def create(self, data: CategoryCreate):

        category = Category(

            nombre=data.nombre,

            descripcion=data.descripcion

        )

        return self.repository.create(category)


    def get_all(self):

        return self.repository.get_all()


    def update(

        self,

        category_id: int,

        data: CategoryUpdate

    ):

        category = self.repository.get_by_id(category_id)

        if category is None:

            raise Exception("Categoría no encontrada.")

        category.nombre = data.nombre
        category.descripcion = data.descripcion
        category.activo = data.activo

        self.repository.update()

        return category


    def delete(self, category_id: int):

        category = self.repository.get_by_id(category_id)

        if category is None:

            raise Exception("Categoría no encontrada.")

        self.repository.delete(category)
