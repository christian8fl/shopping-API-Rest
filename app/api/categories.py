from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user

from app.repositories.category_repository import CategoryRepository

from app.schemas.category import CategoryCreate
from app.schemas.category import CategoryUpdate
from app.schemas.category import CategoryResponse

from app.services.category_service import CategoryService


router = APIRouter(

    prefix="/categories",

    tags=["Categorías"]

)


@router.post(

    "",

    response_model=CategoryResponse

)

def create_category(

    data: CategoryCreate,

    current_user: dict = Depends(get_current_user),

    db: Session = Depends(get_db)

):

    try:

        repository = CategoryRepository(db)

        service = CategoryService(repository)

        return service.create(data)

    except Exception as e:

        raise HTTPException(

            status_code=400,

            detail=str(e)

        )


@router.get(

    "",

    response_model=list[CategoryResponse]

)

def get_categories(

    current_user: dict = Depends(get_current_user),

    db: Session = Depends(get_db)

):

    repository = CategoryRepository(db)

    service = CategoryService(repository)

    return service.get_all()


@router.put(

    "/{category_id}",

    response_model=CategoryResponse

)

def update_category(

    category_id: int,

    data: CategoryUpdate,

    current_user: dict = Depends(get_current_user),

    db: Session = Depends(get_db)

):

    try:

        repository = CategoryRepository(db)

        service = CategoryService(repository)

        return service.update(

            category_id,

            data

        )

    except Exception as e:

        raise HTTPException(

            status_code=400,

            detail=str(e)

        )


@router.delete(

    "/{category_id}"

)

def delete_category(

    category_id: int,

    current_user: dict = Depends(get_current_user),

    db: Session = Depends(get_db)

):

    try:

        repository = CategoryRepository(db)

        service = CategoryService(repository)

        service.delete(category_id)

        return {

            "message": "Categoría eliminada correctamente."

        }

    except Exception as e:

        raise HTTPException(

            status_code=400,

            detail=str(e)

        )
