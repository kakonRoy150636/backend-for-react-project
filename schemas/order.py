from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class OrderBase(BaseModel):
    customer_name: str
    phone: str
    email: EmailStr
    template_id: int
    note: Optional[str] = None

class OrderCreate(OrderBase):
    pass

class OrderResponse(OrderBase):
    id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True