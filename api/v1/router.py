from fastapi import APIRouter
from api.v1.endpoints import auth, templates, categories, orders, analytics, uploads

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(templates.router, prefix="/templates", tags=["Templates"])
api_router.include_router(categories.router, prefix="/categories", tags=["Categories"])
api_router.include_router(orders.router, prefix="/orders", tags=["Orders"])
api_router.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])
api_router.include_router(uploads.router, prefix="/uploads", tags=["Uploads"])