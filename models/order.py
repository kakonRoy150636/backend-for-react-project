from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey, DateTime
from database.base import Base
import enum
import datetime

class OrderStatus(enum.Enum):
    new = "New"
    contacted = "Contacted"
    in_progress = "In Progress"
    completed = "Completed"
    cancelled = "Cancelled"

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(255), nullable=False)
    phone = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False)
    template_id = Column(Integer, ForeignKey("templates.id"))
    status = Column(Enum(OrderStatus), default=OrderStatus.new)
    note = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)