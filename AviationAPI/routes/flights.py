from fastapi import APIRouter, HTTPException
from typing import Optional

from models import FlightCreate, FlightUpdate
from services.flight_service import get_flights_service, get_flight_by_id_service, create_flight_service, \
    update_flight_service, delete_flight_service, get_flight_details_service

router = APIRouter()

@router.get("/flights")
def get_flights(
    limit: int = 20,
    offset: int = 0,
    sort_by: Optional[str] = None,
    sort_order: str = "asc",
    status: Optional[str] = None,
    aircraft_id: Optional[int] = None,
    departure_airport_id: Optional[int] = None,
    arrival_airport_id: Optional[int] = None,
):
    try:
        return get_flights_service(limit, offset, sort_by, sort_order,status, aircraft_id, departure_airport_id, arrival_airport_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid query parameters")

@router.post("/flight")
def create_flight(flight: FlightCreate):
    try:
        return create_flight_service(flight)
    except ValueError:
        raise HTTPException(status_code=400, detail="Flight already exists")

@router.get("/flight/{flight_id}")
def get_flight(flight_id: int):
    try:
        return get_flight_by_id_service(flight_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Flight not found")

@router.delete("/flight/{flight_id}")
def delete_flight(flight_id: int):
    try:
        return delete_flight_service(flight_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Flight not found")

@router.put("/flight/{flight_id}")
def update_flight(flight_id: int, update: FlightUpdate):
    try:
        return update_flight_service(flight_id, update)
    except ValueError:
        raise HTTPException(status_code=404, detail="Flight not found")

@router.get("/flight/{flight_id}/details")
def get_flight_details(flight_id: int):
    try:
        return get_flight_details_service(flight_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Flight not found")



