from sqlmodel import Session, select
from datetime import datetime
from database.db import engine

from models import Flight, FlightUpdate

def get_all_flights():
    with Session(engine) as session:
        statement = select(Flight)
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


