from app.web.core.users.views import router as users_router

from fastapi import APIRouter

router = APIRouter()


router.include_router(prefix="/v1", router=users_router, tags=["users"])
