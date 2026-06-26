from fastapi import Request
from repositories.tracker_repo import get_canary
from core.exceptions import CanaryNotFound

async def get_ip_adress(request: Request):
    x_forwarded_for = request.headers.get('x_forwarded_for')
    if x_forwarded_for:
        client_ip = x_forwarded_for.split(',')[0].strip()
    else:
        client_ip = request.client.host if request.client else 'unknown'

    return client_ip

async def proccess_the_target(session, token: str, request: Request):
    canary = await get_canary(session, token)
    if not canary: raise CanaryNotFound
    
    ip_address = await get_ip_adress(request)
    user_agent = request.headers.get('user-agent')