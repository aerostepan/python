from models import Runway, RunwayCreate, RunwayUpdate
from database.runway_repo import get_all_runways, get_runway_by_id, save_runway, delete_runway, update_runway

def get_runways_service():
    return get_all_runways()

def get_runway_by_id_service(runway_id):
    runway = get_runway_by_id(runway_id)
    if runway is None:
        raise ValueError()
    return runway

def create_runway_service(runway: RunwayCreate):
    new_runway = Runway(
        airport_id = runway.airport_id,
        runway_code = runway.runway_code,
        length_meters = runway.length_meters,
        surface_type = runway.surface_type,
    )
    saved_runway = save_runway(new_runway)
    return {
        "message": "Runway created successfully",
        "runway": saved_runway,
    }

def delete_runway_service(runway_id: int):
    existing_runway = delete_runway(runway_id)
    if existing_runway is not None:
        return {
            "message": "Runway deleted successfully",
            "runway": existing_runway,
        }
    raise ValueError()

def update_runway_service(runway_id: int, runway: RunwayUpdate):
    runway = update_runway(runway_id, runway)
    if runway is not None:
        return {
            "message": "Runway updated successfully",
            "runway": runway,
        }
    raise ValueError()


