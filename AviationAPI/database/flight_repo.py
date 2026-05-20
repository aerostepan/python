from sqlmodel import Session, select
from datetime import datetime
from database.db import engine

from models import Flight, FlightUpdate

def get_all_flights(limit = None, offset = None,sort_by = None,sort_order = None):
    with Session(engine) as session:

        allowed_sort_fields = {
            "id": Flight.id,
            "flight_number": Flight.flight_number,
            "scheduled_departure": Flight.scheduled_departure,
            "scheduled_arrival": Flight.scheduled_arrival,
            "status": Flight.status,
        }

        statement = select(Flight)

        if sort_by is not None:
            column = allowed_sort_fields[sort_by]
            if sort_order == "desc":
                statement = statement.order_by(column.desc())
            else:
                statement = statement.order_by(column.asc())
        if limit is not None:
            statement = statement.limit(limit)
        if offset is not None:
            statement = statement.offset(offset)
        result = session.exec(statement)
        return result.all()

def get_flight_by_id(flight_id):
    with Session(engine) as session:
        statement = select(Flight).where(Flight.id == flight_id)
        flight = session.exec(statement).first()
        return flight

def save_flight(new_flight):
    with Session(engine) as session:
        session.add(new_flight)
        session.commit()
        session.refresh(new_flight)
        return new_flight

def delete_flight(flight_id):
    with Session(engine) as session:
        statement = select(Flight).where(Flight.id == flight_id)
        flight = session.exec(statement).first()
        if flight is None:
            return None
        session.delete(flight)
        session.commit()
        return flight

def update_flight(flight_id, new_flight_data: FlightUpdate):
    with Session(engine) as session:
        statement = select(Flight).where(Flight.id == flight_id)
        flight = session.exec(statement).first()
        if flight is None:
            return None
        for key, value in new_flight_data.model_dump().items():
            setattr(flight, key, value)
        session.commit()
        session.refresh(flight)
        return flight

def get_flight_details_by_id(flight_id):
    with Session(engine) as session:
        statement = select(Flight).where(Flight.id == flight_id)
        flight = session.exec(statement).first()
        if flight is None:
            return None
        return {
            "id": flight.id,
            "flight_number": flight.flight_number,
            "status": flight.status,
            "scheduled_departure": flight.scheduled_departure,
            "scheduled_arrival": flight.scheduled_arrival,
            "aircraft": flight.aircraft,
            "departure_airport": flight.departure_airport,
            "arrival_airport": flight.arrival_airport,

        }
def filter_flights(status = None, aircraft_id = None, departure_airport = None, arrival_airport = None):
    with Session(engine) as session:
        statement = select(Flight)
        if status is not None:
            statement = statement.where(Flight.status == status)
        if aircraft_id is not None:
            statement = statement.where(Flight.aircraft_id == aircraft_id)
        if departure_airport is not None:
            statement = statement.where(Flight.departure_airport == departure_airport)
        if arrival_airport is not None:
            statement = statement.where(Flight.arrival_airport == arrival_airport)
        result = session.exec(statement)
        return result.all()

