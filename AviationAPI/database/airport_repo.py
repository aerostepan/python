from sqlmodel import Session, select
from database.db import engine

from models import Airport, AirportUpdate


def get_all_airports():
    with Session(engine) as session:
        statement = select(Airport)
        result = session.exec(statement)
        return result.all()


def get_airport_by_icao(icao):
    with Session(engine) as session:
        statement = select(Airport).where(Airport.icao == icao)
        result = session.exec(statement)
        return result.first()

def save_airport(new_airport):
    with Session(engine) as session:
        session.add(new_airport)
        session.commit()
        session.refresh(new_airport)
        return new_airport

def delete_airport(icao):
    with Session(engine) as session:
        statement = select(Airport).where(Airport.icao == icao)
        airport = session.exec(statement).first()
        if airport is None:
            return None
        session.delete(airport)
        session.commit()
        return airport

def update_airport(icao, update_data: AirportUpdate):
    with Session(engine) as session:
        statement = select(Airport).where(Airport.icao == icao)
        airport = session.exec(statement).first()
        if airport is None:
            return None
        for key, value in update_data.model_dump().items():
            setattr(airport, key, value)
        session.commit()
        session.refresh(airport)
        return airport



