from models import AirportCreate, AirportUpdate, AirportResponse
from database.storage import airports, airport_id_counter


def get_all_airports():
    return airports

def get_airport_by_icao(icao):
    for airport in airports:
        if airport.get("icao") == icao:
            return airport
    raise ValueError("Airport not found")


def create_airport(airport: AirportCreate):
    for existing_airport in airports:
        if existing_airport.get("icao") == airport.icao:
            raise ValueError("Airport already exists")
    #airports.append(airport.model_dump())
    new_airport = airport.model_dump()
    new_airport["id"] = airport_id_counter["next_id"]
    airports.append(new_airport)
    airport_id_counter["next_id"] = airport_id_counter["next_id"] + 1
    return {
        "message": "Airport created",
        "airport": new_airport
    }

def delete_airport(icao: str):
    for existing_airport in airports:
        if existing_airport.get("icao") == icao:
            airports.remove(existing_airport)
            return {
                "message": "Airport deleted",
            }
    raise ValueError("Airport not found")

def update_airport(icao: str, airport: AirportUpdate):
    for existing_airport in airports:
        if existing_airport.get("icao") == icao:
            existing_airport.update(airport.model_dump())
            return {
                "message": "Airport updated",
                "airport": existing_airport
            }
    raise ValueError("Airport not found")


