from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings
from database.base import Base

# Neon ডাটাবেসের সাথে কানেকশন তৈরি করছি
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

# ডাটাবেস সেশন তৈরি করছি
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# এটি FastAPI এর dependency হিসেবে কাজ করবে
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()