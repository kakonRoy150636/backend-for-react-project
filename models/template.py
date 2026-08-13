from sqlalchemy import Column, String, Text, Float, Boolean, Enum, ForeignKey, DateTime, Integer
from sqlalchemy.orm import relationship
from database.base import Base
import datetime
import enum

class TemplateStatus(enum.Enum):
    draft = "draft"
    published = "published"

class Template(Base):
    __tablename__ = "templates"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    slug = Column(String(255), unique=True, index=True, nullable=False)
    description = Column(Text, nullable=True)
    thumbnail_url = Column(String(500), nullable=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    technology = Column(String(255), nullable=True) # E.g., "React, Node, Tailwind"
    price = Column(Float, default=0.0)
    live_preview_url = Column(String(500), nullable=True)
    featured = Column(Boolean, default=False)
    trending = Column(Boolean, default=False)
    status = Column(Enum(TemplateStatus), default=TemplateStatus.draft)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    category = relationship("Category")
    screenshots = relationship("Screenshot", back_populates="template", cascade="all, delete-orphan")

class Screenshot(Base):
    __tablename__ = "screenshots"
    id = Column(Integer, primary_key=True, index=True)
    template_id = Column(Integer, ForeignKey("templates.id"))
    image_url = Column(String(500), nullable=False)

    template = relationship("Template", back_populates="screenshots")