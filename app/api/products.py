from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user

from app.repositories.category_repository import CategoryRepository
from app.repositories.product_repository import ProductRepository

from app.schemas.product import ProductCreate
from app.schemas.product import ProductUpdate
from app.schemas.product import ProductResponse

from app.services.product_service import ProductService


router = APIRouter(

    prefix="/products",

    tags=["Productos"]

)


@router.post(
    "",
    response_model=ProductResponse
)
def create_product(

    data: ProductCreate,

    current_user: dict = Depends(get_current_user),

    db: Session = Depends(get_db)

):

    try:

        repository = ProductRepository(db)

        category_repository = CategoryRepository(db)

        service = ProductService(
            repository,
            category_repository
        )

        return service.create(data)

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "",
    response_model=list[ProductResponse]
)
def get_products(

    current_user: dict = Depends(get_current_user),

    db: Session = Depends(get_db)

):

    repository = ProductRepository(db)

    category_repository = CategoryRepository(db)

    service = ProductService(
        repository,
        category_repository
    )

    return service.get_all()


@router.put(
    "/{product_id}",
    response_model=ProductResponse
)
def update_product(

    product_id: int,

    data: ProductUpdate,

    current_user: dict = Depends(get_current_user),

    db: Session = Depends(get_db)

):

    try:

        repository = ProductRepository(db)

        category_repository = CategoryRepository(db)

        service = ProductService(
            repository,
            category_repository
        )

        return service.update(
            product_id,
            data
        )

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete(
    "/{product_id}"
)
def delete_product(

    product_id: int,

    current_user: dict = Depends(get_current_user),

    db: Session = Depends(get_db)

):

    try:

        repository = ProductRepository(db)

        category_repository = CategoryRepository(db)

        service = ProductService(
            repository,
            category_repository
        )

        service.delete(product_id)

        return {
            "message": "Producto eliminado correctamente."
        }

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
