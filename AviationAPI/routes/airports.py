from fastapi import APIRouter, HTTPException


from models import AirportCreate, AirportUpdate, AirportResponse
from services.airport_service import get_all_airports, get_airport_by_icao, create_airport, delete_airport, update_airport

router = APIRouter()

@router.get("/airports/{icao}")
def get_airports_icao(icao: str):
    try:
        return get_airport_by_icao(icao)
    except ValueError:
        raise HTTPException(status_code=404, detail="Airport not found")

@router.get("/airports")
def get_airports():
        return get_all_airports()

@router.post("/airports")
def create_route_airport(airport: AirportCreate):
    try:
        return create_airport(airport)
    except ValueError:
        raise HTTPException(status_code=400, detail="Airport already exists")

@router.delete("/airports/{icao}")
def delete_route_airport(icao: str):
    try:
        return delete_airport(icao)
    except ValueError:
        raise HTTPException(status_code=404, detail="Airport not found")

@router.put("/airports/{icao}")
def update_route_airport(icao: str, airport: AirportUpdate):
    try:
        return update_airport(icao, airport)
    except ValueError:
        raise HTTPException(status_code=404, detail="Airport not found")
