from fastapi import APIRouter

from models import Airport
from database import airports

router = APIRouter()

@router.get("/airports")
def get_airports():
    return airports

@router.post("/airports")
def create_airport(airport: Airport):

    airports.append(airports.model_dump())
    return {
        "message": "Airport created",
        "airport": airport
    }


