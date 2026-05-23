
from database.aircraft_repo import get_aircraft_by_id
from database.airport_repo import get_airport_by_id
from models import Flight,FlightCreate,FlightUpdate, FlightDetailedResponse
from database.flight_repo import get_all_flights,save_flight,delete_flight,update_flight,get_flight_details_by_id, get_flight_by_id



def get_flights_service(limit = None, offset = None,sort_by = None,sort_order = None, status = None,aircraft_id = None,departure_airport_id = None,arrival_airport_id = None):
    if limit is not None and limit <= 0:
        raise ValueError()
    if offset is not None and offset < 0:
        raise ValueError()
    if sort_order is not None and sort_order not in ['asc', 'desc']:
        raise ValueError()
    if sort_by is not None and sort_by not in ['id','flight_number','scheduled_departure','scheduled_arrival','status']:
        raise ValueError()
    if aircraft_id is not None and aircraft_id <= 0:
        raise ValueError()
    if departure_airport_id is not None and departure_airport_id <= 0:
        raise ValueError()
    if arrival_airport_id is not None and arrival_airport_id <= 0:
        raise ValueError()
    if status is not None and status not in ['scheduled','delayed','cancelled']:
        raise ValueError()


    return get_all_flights(limit, offset, sort_by, sort_order, status, aircraft_id, departure_airport_id, arrival_airport_id)

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

