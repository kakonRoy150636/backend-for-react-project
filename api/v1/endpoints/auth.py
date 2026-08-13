from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.session import get_db
from schemas.user import AdminLogin
from schemas.token import Token, RefreshTokenRequest
from models.user import Admin
from services.auth_service import verify_password
from auth.jwt_handler import create_access_token, create_refresh_token
import jwt
from core.config import settings

router = APIRouter()

@router.post("/login", response_model=Token)
def login(payload: AdminLogin, db: Session = Depends(get_db)):
    admin = db.query(Admin).filter(Admin.email == payload.email).first()
    if not admin or not verify_password(payload.password, admin.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": str(admin.id)})
    refresh_token = create_refresh_token(data={"sub": str(admin.id)})
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

@router.post("/refresh", response_model=Token)
def refresh_token(payload: RefreshTokenRequest):
    try:
        decoded = jwt.decode(payload.refresh_token, settings.JWT_SECRET, algorithms=[settings.ALGORITHM])
        admin_id = decoded.get("sub")
        access_token = create_access_token(data={"sub": admin_id})
        return {"access_token": access_token, "refresh_token": payload.refresh_token, "token_type": "bearer"}
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")