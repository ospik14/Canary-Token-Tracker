from pydantic import BaseModel

class IpAdditionalData(BaseModel):
    country: str
    city: str
    isp: str
