from fastapi import APIRouter

from app.web.core.users.router import router as users_router

router = APIRouter()


router.include_router(prefix="/v1", router=users_router, tags=["users"])
