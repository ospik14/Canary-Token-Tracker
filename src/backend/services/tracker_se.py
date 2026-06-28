from fastapi import Request
from backend.repositories.tracker_repo import get_canary, add_visit
from backend.core.exceptions import CanaryNotFound
from backend.clients.ipapi import get_add_data
from backend.models.visits import Visits

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
    
    client_ip = await get_ip_adress(request)
    add_data = await get_add_data(client_ip)
    
    visit = await add_visit(
        Visits(
            canary_id = canary.id,
            ip_adress = client_ip,
            user_agent = request.headers.get('user-agent'),
            country = add_data.country,
            city = add_data.city,
            isp = add_data.isp
        )
    )

    return visit



