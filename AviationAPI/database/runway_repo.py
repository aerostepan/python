from sqlmodel import Session, select
from database.db import engine

from models import Runway, RunwayUpdate

def get_all_runways():
    with Session(engine) as session:
        statement = select(Runway)
        result = session.exec(statement)
        return result.all()

def get_runway_by_id(runway_id):
    with Session(engine) as session:
        statement = select(Runway).where(Runway.id == runway_id)
        runway = session.exec(statement).first()
        return runway

def save_runway(new_runway: Runway):
    with Session(engine) as session:
        session.add(new_runway)
        session.commit()
        session.refresh(new_runway)
        return new_runway

def delete_runway(runway_id):
    with Session(engine) as session:
        statement = select(Runway).where(Runway.id == runway_id)
        runway = session.exec(statement).first()
        if runway is None:
            return None
        session.delete(runway)
        session.commit()
        return runway

def update_runway(runway_id, new_runway_data: RunwayUpdate):
    with Session(engine) as session:
        statement = select(Runway).where(Runway.id == runway_id)
        runway = session.exec(statement).first()
        if runway is None:
            return None
        for key, value in new_runway_data.model_dump().items():
            setattr(runway, key, value)
        session.commit()
        session.refresh(runway)
        return runway

