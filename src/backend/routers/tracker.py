from fastapi import APIRouter, Request
from backend.services.tracker_se import proccess_the_target
from backend.depends import db_dep
router = APIRouter(
    tags=['tracker']
)

@router.get('/t/{token}')
async def track_click(session: db_dep, token: str, request: Request):
    return await proccess_the_target(token, request)

    