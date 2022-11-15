from fastapi import APIRouter

from controllers import item_controller as items

router = APIRouter()

router.include_router(items.router, prefix='/items')