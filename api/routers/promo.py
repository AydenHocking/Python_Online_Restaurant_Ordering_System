from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import promo as controller
from ..schemas import promo as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Promos'],
    prefix="/promos"
)

@router.post("/", response_model=schema.Promo)
def create(request: schema.PromoCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.Promo])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/apply")
def apply_promo(code: str, db: Session = Depends(get_db)):
    return controller.apply_promo_code(db, code)

@router.get("/{item_id}", response_model=schema.Promo)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)

@router.put("/{item_id}", response_model=schema.Promo)
def update(item_id: int, request: schema.PromoUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)


