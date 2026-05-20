from fastapi import APIRouter

from database.aircraft_repo import get_aircraft_by_id
from database.airport_repo import get_airport_by_id
from models import Flight,FlightCreate,FlightUpdate, FlightDetailedResponse
from database.flight_repo import get_all_flights,save_flight,delete_flight,update_flight,get_flight_details_by_id, get_flight_by_id



def get_flights_service():
    return get_all_flights()

def get_flight_by_id_service(flight_id):
    flight = get_flight_by_id(flight_id)
    if flight is None:
        raise ValueError()
    return flight

def create_flight_service(flight:FlightCreate):
    aircraft = get_aircraft_by_id(flight.aircraft_id)
    if aircraft is None:
        raise ValueError()
    departure_airport = get_airport_by_id(flight.departure_airport_id)
    if departure_airport is None:
        raise ValueError()
    arrival_airport = get_airport_by_id(flight.arrival_airport_id)
    if arrival_airport is None:
        raise ValueError()
    if flight.departure_airport_id == flight.arrival_airport_id:
        raise ValueError()
    new_flight = Flight(
        flight_number=flight.flight_number,
        aircraft_id=flight.aircraft_id,
        departure_airport_id=flight.departure_airport_id,
        arrival_airport_id=flight.arrival_airport_id,
        scheduled_departure = flight.scheduled_departure,
        scheduled_arrival = flight.scheduled_arrival,
        status = flight.status,

    )
    saved_flight = save_flight(new_flight)
    return{
        "message": "Flight created successfully",
        "flight": saved_flight
    }



def delete_flight_service(flight_id):
    existing_flight = delete_flight(flight_id)
    if existing_flight is not None:
        return{
            "message": "Flight deleted successfully",
            "flight": existing_flight
        }
    raise ValueError()

def update_flight_service(flight_id, flight:FlightUpdate):
    flight = update_flight(flight_id, flight)
    if flight is not None:
        return{
            "message": "Flight updated successfully",
            "flight": flight
        }
    raise ValueError()

def get_flight_details_service(flight_id):
    flight = get_flight_details_by_id(flight_id)
    if flight is None:
        raise ValueError()
    return flight
