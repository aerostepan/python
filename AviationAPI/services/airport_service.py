from models import AirportCreate, AirportUpdate, Airport

from database.airport_repo import get_all_airports, get_airport_by_icao, save_airport, delete_airport, update_airport


def get_all_airports_service():
    return get_all_airports()

def get_airport_by_icao_service(icao):
    airport = get_airport_by_icao(icao)
    if airport is None:
        raise ValueError("Airport not found")
    return airport

def create_airport_service(airport: AirportCreate):
    new_airport = Airport(
        icao=airport.icao,
        iata=airport.iata,
        name=airport.name,
        city=airport.city,
        country=airport.country,
    )
    existing_airport = get_airport_by_icao(airport.icao)
    if existing_airport is None:
        raise ValueError("Airport already exists")
    save_airport(new_airport)
    return {
        "message": "Airport created",
        "airport": new_airport
    }

def delete_airport_service(icao: str):
    existing_airport = delete_airport(icao)
    if existing_airport is not None:
        return {
            "message": "Airport deleted",
            "airport": existing_airport
        }
    raise ValueError("Airport not found")

def update_airport_service(icao: str, airport: AirportUpdate):
    airport = update_airport(icao, airport)
    if airport is not None:
        return {
            "message": "Airport updated",
            "airport": airport
        }
    raise ValueError("Airport not found")


