from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum
from database.base import Base
import enum
import datetime

class EventType(enum.Enum):
    homepage_view = "homepage_view"
    template_view = "template_view"
    order_click = "order_click"

class AnalyticsEvent(Base):
    __tablename__ = "analytics_events"

    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(Enum(EventType), nullable=False)
    template_id = Column(Integer, ForeignKey("templates.id"), nullable=True)
    # Python 3.13+ compatible UTC time
    created_at = Column(DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc))