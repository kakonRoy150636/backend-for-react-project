from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database.session import get_db
from auth.dependencies import get_current_admin
from models.order import Order
from schemas.order import OrderCreate, OrderResponse

router = APIRouter()

@router.post("/", response_model=OrderResponse)
def create_order(payload: OrderCreate, db: Session = Depends(get_db)):
    order = Order(**payload.dict())
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

@router.get("/", response_model=List[OrderResponse], dependencies=[Depends(get_current_admin)])
def get_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()