from models import Airport
from database import airports

def get_all_airports():
    return airports

def get_airport_by_icao(icao):
    for airport in airports:
        if airport.get("icao") == icao:
            return airport
    raise ValueError("Airport not found")


def create_airport(airport: Airport):
    for existing_airport in airports:
        if existing_airport.get("icao") == airport.icao:
            raise ValueError("Airport already exists")
    airports.append(airport.model_dump())
    return {
        "message": "Airport created",
        "airport": airport
    }

def delete_airport(icao: str):
    for existing_airport in airports:
        if existing_airport.get("icao") == icao:
            airports.remove(existing_airport)
            return {
                "message": "Airport deleted",
            }
    raise ValueError("Airport not found")
