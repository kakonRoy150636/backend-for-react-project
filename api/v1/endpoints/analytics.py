from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.session import get_db
from auth.dependencies import get_current_admin
from services.analytics_service import get_dashboard_stats

router = APIRouter()

@router.post("/track")
def track_event(event_data: dict, db: Session = Depends(get_db)):
    return {"success": True, "message": "Event tracked"}

@router.get("/stats", dependencies=[Depends(get_current_admin)])
def get_analytics_stats(db: Session = Depends(get_db)):
    stats = get_dashboard_stats(db)
    return stats