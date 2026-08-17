from app.models.product import Product

from app.repositories.category_repository import CategoryRepository
from app.repositories.product_repository import ProductRepository

from app.schemas.product import ProductCreate
from app.schemas.product import ProductUpdate


class ProductService:

    def __init__(
        self,
        repository: ProductRepository,
        category_repository: CategoryRepository
    ):

        self.repository = repository
        self.category_repository = category_repository

    def create(self, data: ProductCreate):

        category = self.category_repository.get_by_id(
            data.categoria_id
        )

        if category is None:
            raise Exception("La categoría no existe.")

        product = Product(

            categoria_id=data.categoria_id,

            nombre=data.nombre,

            descripcion=data.descripcion,

            precio=data.precio,

            stock=data.stock,

            imagen=data.imagen

        )

        return self.repository.create(product)

    def get_all(self):

        return self.repository.get_all()

    def update(
        self,
        product_id: int,
        data: ProductUpdate
    ):

        product = self.repository.get_by_id(product_id)

        if product is None:
            raise Exception("Producto no encontrado.")

        category = self.category_repository.get_by_id(
            data.categoria_id
        )

        if category is None:
            raise Exception("La categoría no existe.")

        product.categoria_id = data.categoria_id
        product.nombre = data.nombre
        product.descripcion = data.descripcion
        product.precio = data.precio
        product.stock = data.stock
        product.imagen = data.imagen
        product.activo = data.activo

        self.repository.update()

        return product

    def delete(self, product_id: int):

        product = self.repository.get_by_id(product_id)

        if product is None:
            raise Exception("Producto no encontrado.")

        self.repository.delete(product)

