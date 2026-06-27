from httpx import AsyncClient
from schemas.additional_data import IpAdditionalData

async def get_location(client_ip: str):
    async with AsyncClient() as client:
        response = await client.get(f'https://ipapi.co/{client_ip}/json/')
        if response.status_code == 200: 
            data=response.json()
            return IpAdditionalData(
                country = data.get("country_name"),
                city = data.get("city"),
                isp = data.get("org")
            )
        else:
            return IpAdditionalData(
                city='Undefined', 
                country='Undefined'
            )
        