from fastapi import APIRouter, HTTPException
from models import AircraftCreate, AircraftUpdate
from services.aircraft_sevice import get_all_aircraft_service,get_aircraft_by_reg_service,create_aircraft_service,update_aircraft_service, delete_aircraft_service

router = APIRouter()

@router.get("/aircrafts")
def get_aircrafts():
    return get_all_aircraft_service()

@router.get("/aircrafts/{registration}")
def get_aircraft_reg(registration):
    try:
        return get_aircraft_by_reg_service(registration)
    except ValueError:
        raise HTTPException(status_code=404, detail="Aircraft not found")

@router.post("/aircraft")
def create_aircraft(aircraft: AircraftCreate):
    try:
        return create_aircraft_service(aircraft)
    except ValueError:
        raise HTTPException(status_code=400, detail="Aircraft already exists")

@router.delete("/aircraft/{registration}")
def delete_aircraft(registration: str):
    try:
        return delete_aircraft_service(registration)
    except ValueError:
        raise HTTPException(status_code=404, detail="Aircraft not found")

@router.put("/aircraft/{registration}")
def update_aircraft(registration: str, aircraft: AircraftUpdate):
    try:
        return update_aircraft_service(registration, aircraft)
    except ValueError:
        raise HTTPException(status_code=404, detail="Aircraft not found")

