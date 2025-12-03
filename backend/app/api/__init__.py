from fastapi import APIRouter
from app.api import auth_router, profile_router, meeting_router, application_router, review_router

api_router = APIRouter()
api_router.include_router(auth_router.router)
api_router.include_router(profile_router.router)
api_router.include_router(meeting_router.router)
api_router.include_router(application_router.router)
api_router.include_router(review_router.router)
