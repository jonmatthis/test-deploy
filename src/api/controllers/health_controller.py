import requests
from fastapi import APIRouter
from pydantic import BaseModel


health_check_router = APIRouter()


class HealthCheckResponse(BaseModel):
    message: str = "OK"


@health_check_router.get('/healthcheck', tags=['general'])
@health_check_router.get('/health', tags=['general'])
def route():
    try:
        requests.get('http://google.com')
    except:
        raise ValueError("Unhealthy")
    else:
        return HealthCheckResponse()
