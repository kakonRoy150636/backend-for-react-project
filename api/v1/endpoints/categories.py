from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database.session import get_db
from auth.dependencies import get_current_admin
from models.category import Category
from schemas.category import CategoryCreate, CategoryResponse
from utils.slug import generate_slug

router = APIRouter()

@router.get("/", response_model=List[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()

@router.post("/", response_model=CategoryResponse, dependencies=[Depends(get_current_admin)])
def create_category(payload: CategoryCreate, db: Session = Depends(get_db)):
    category = Category(name=payload.name, slug=generate_slug(payload.name))
    db.add(category)
    db.commit()
    db.refresh(category)
    return category