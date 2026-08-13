from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from models.analytics import AnalyticsEvent
from models.template import Template
from models.order import Order

def get_dashboard_stats(db: Session):
    # View counts
    homepage_views = db.query(AnalyticsEvent).filter(AnalyticsEvent.event_type == "homepage_view").count()
    template_views = db.query(AnalyticsEvent).filter(AnalyticsEvent.event_type == "template_view").count()
    order_clicks = db.query(AnalyticsEvent).filter(AnalyticsEvent.event_type == "order_click").count()
    
    # Conversions
    total_orders = db.query(Order).count()
    conversion_rate = (total_orders / order_clicks * 100) if order_clicks > 0 else 0.0

    # Most Viewed Templates
    most_viewed = db.query(
        Template.title, func.count(AnalyticsEvent.id).label('views')
    ).join(AnalyticsEvent, AnalyticsEvent.template_id == Template.id) \
     .filter(AnalyticsEvent.event_type == "template_view") \
     .group_by(Template.id).order_by(desc('views')).limit(5).all()

    return {
        "homepage_views": homepage_views,
        "template_views": template_views,
        "order_clicks": order_clicks,
        "conversion_rate": round(conversion_rate, 2),
        "most_viewed_templates": [{"title": t, "views": v} for t, v in most_viewed]
    }