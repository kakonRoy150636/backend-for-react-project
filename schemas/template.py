from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class ScreenshotBase(BaseModel):
    image_url: str

class TemplateBase(BaseModel):
    title: str
    description: Optional[str] = None
    category_id: int
    technology: Optional[str] = None
    price: float = 0.0
    live_preview_url: Optional[str] = None

class TemplateCreate(TemplateBase):
    pass

class TemplateUpdate(BaseModel):
    title: Optional[str] = None
    featured: Optional[bool] = None
    trending: Optional[bool] = None
    status: Optional[str] = None

class TemplateResponse(TemplateBase):
    id: int
    slug: str
    thumbnail_url: Optional[str] = None
    featured: bool
    trending: bool
    status: str
    created_at: datetime
    screenshots: List[ScreenshotBase] = []

    class Config:
        from_attributes = True