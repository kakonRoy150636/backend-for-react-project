from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database.session import get_db
from auth.dependencies import get_current_admin
from models.template import Template
from schemas.template import TemplateCreate, TemplateResponse, TemplateUpdate
from utils.slug import generate_slug

router = APIRouter()

@router.get("/", response_model=List[TemplateResponse])
def get_templates(db: Session = Depends(get_db)):
    templates = db.query(Template).all()
    return templates

@router.get("/{slug}", response_model=TemplateResponse)
def get_template_by_slug(slug: str, db: Session = Depends(get_db)):
    template = db.query(Template).filter(Template.slug == slug).first()
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    return template

@router.post("/", response_model=TemplateResponse, status_code=201, dependencies=[Depends(get_current_admin)])
def create_template(payload: TemplateCreate, db: Session = Depends(get_db)):
    db_template = Template(
        **payload.dict(),
        slug=generate_slug(payload.title),
        status="draft"
    )
    db.add(db_template)
    db.commit()
    db.refresh(db_template)
    return db_template

@router.patch("/{template_id}", response_model=TemplateResponse, dependencies=[Depends(get_current_admin)])
def update_template(template_id: int, payload: TemplateUpdate, db: Session = Depends(get_db)):
    template = db.query(Template).filter(Template.id == template_id).first()
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    
    update_data = payload.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(template, key, value)
    
    db.commit()
    db.refresh(template)
    return template