from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import review as controller
from ..schemas import review as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Reviews'],
    prefix="/reviews"
)

@router.post("/", response_model=schema.Review)
def create(request: schema.ReviewCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/sorted")
def get_reviews_sorted(sort_by: str = None, db: Session = Depends(get_db)):
    return controller.read_all_sorted(db, sort_by)

@router.get("/", response_model=list[schema.Review])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{item_id}", response_model=schema.Review)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)

@router.put("/{item_id}", response_model=schema.Review)
def update(item_id: int, request: schema.ReviewUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)


