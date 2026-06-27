from fastapi import APIRouter, Request
from services.tracker_se import proccess_the_target

router = APIRouter(
    tags=['tracker']
)

@router.get('/t/{token}')
async def track_click(token: str, request: Request):
    return await proccess_the_target(token, request)

    