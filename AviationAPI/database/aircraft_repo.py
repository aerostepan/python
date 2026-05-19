from sqlmodel import Session, select
from database.db import engine

from models import Aircraft, AircraftUpdate

def get_all_aircraft():
    with Session(engine) as session:
        statement = select(Aircraft)
        result = session.exec(statement)
        return result.all()

def get_aircraft_by_reg(registration):
    with Session(engine) as session:
        statement = select(Aircraft).where(Aircraft.registration == registration)
        result = session.exec(statement)
        return result.first()

def save_aircraft(new_aircraft: Aircraft):
    with Session(engine) as session:
        session.add(new_aircraft)
        session.commit()
        session.refresh(new_aircraft)
        return new_aircraft

def delete_aircraft(registration):
    with Session(engine) as session:
        statement = select(Aircraft).where(Aircraft.registration == registration)
        aircraft = session.exec(statement).first()
        if aircraft is None:
            return None
        session.delete(aircraft)
        session.commit()
        return aircraft

def update_aircraft(registration, new_aircraft_data: AircraftUpdate):
    with Session(engine) as session:
        statement = select(Aircraft).where(Aircraft.registration == registration)
        aircraft = session.exec(statement).first()
        if aircraft is None:
            return None
        for key, value in new_aircraft_data.model_dump().items():
            setattr(aircraft, key, value)
        session.commit()
        session.refresh(aircraft)
        return aircraft

def get_aircraft_by_id(aircraft_id):
    with Session(engine) as session:
        statement = select(Aircraft).where(Aircraft.id == aircraft_id)
        aircraft = session.exec(statement).first()
        return aircraft