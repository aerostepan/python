from models import Aircraft, AircraftCreate, AircraftUpdate
from database.aircraft_repo import get_all_aircraft,get_aircraft_by_reg,save_aircraft,delete_aircraft,update_aircraft

def get_all_aircraft_service():
    return get_all_aircraft()

def get_aircraft_by_reg_service(registration):
    aircraft = get_aircraft_by_reg(registration)
    if aircraft is None:
        raise ValueError()
    return aircraft

def create_aircraft_service(aircraft: AircraftCreate):
    new_aircraft = Aircraft(
        registration=aircraft.registration,
        icao_type=aircraft.icao_type,
        manufacturer=aircraft.manufacturer,
        model=aircraft.model,
        operator=aircraft.operator,
        status=aircraft.status,
    )
    existing_aircraft = get_aircraft_by_reg(aircraft.registration)
    if existing_aircraft is not None:
        raise ValueError()
    save_aircraft(new_aircraft)
    return {
        "message": "Aircraft created successfully",
        "aircraft": new_aircraft,
    }

def delete_aircraft_service(registration):
    existing_aircraft = delete_aircraft(registration)
    if existing_aircraft is not None:
        return {
            "message": "Aircraft deleted successfully",
            "aircraft": existing_aircraft,
        }
    raise ValueError()

def update_aircraft_service(registration, aircraft: AircraftUpdate):
    aircraft = update_aircraft(registration, aircraft)
    if aircraft is not None:
        return {
            "message": "Aircraft updated successfully",
            "aircraft": aircraft,
        }
    raise ValueError()