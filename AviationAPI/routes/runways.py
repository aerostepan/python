from fastapi import APIRouter, HTTPException

from models import RunwayCreate, RunwayUpdate
from services.runway_service import get_runways_service, get_runway_by_id_service, delete_runway_service, update_runway_service, create_runway_service

router = APIRouter()

@router.get("/runways")
def get_runways():
    return get_runways_service()

@router.get("/runways/{runway_id}")
def get_runway_by_id(runway_id: int):
    try:
        return get_runway_by_id_service(runway_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Runway not found")

@router.post("/runways")
def create_runway(runway: RunwayCreate):
    try:
        return create_runway_service(runway)
    except ValueError:
        raise HTTPException(status_code=400, detail="Runway already exists")

@router.delete("/runways/{runway_id}")
def delete_runway(runway_id: int):
    try:
        return delete_runway_service(runway_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Runway not found")

@router.put("/runways/{runway_id}")
def update_runway(runway_id: int, runway: RunwayUpdate):
    try:
        return update_runway_service(runway_id, runway)
    except ValueError:
        raise HTTPException(status_code=404, detail="Runway not found")

