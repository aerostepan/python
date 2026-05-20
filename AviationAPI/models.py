
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship

class Airport(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    icao: str = Field(min_length=4, max_length=4)
    iata: str = Field(min_length=3, max_length=3)
    name: str
    city: str
    country: str
    runways: List["Runway"] = Relationship(back_populates="airport")

class AirportCreate(BaseModel):
    icao: str = Field(min_length=4, max_length=4)
    iata: str = Field(min_length=3, max_length=3)
    name: str
    city: str
    country: str

class AirportUpdate(BaseModel):
    name: str
    city: str
    country: str

class AirportResponse(BaseModel):
    id: int
    icao: str
    iata: str
    name: str
    city: str
    country: str

class Runway(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    airport_id: int = Field(foreign_key="airport.id")
    runway_code: str
    length_meters: int
    surface_type: str
    airport: Optional[Optional["Airport"]] = Relationship(back_populates="runways")


class RunwayCreate(BaseModel):
    airport_id: int
    runway_code: str
    length_meters: int
    surface_type: str

class RunwayUpdate(BaseModel):
    length_meters: int
    surface_type: str

class RunwayResponse(BaseModel):
    id: int
    airport_id: int
    runway_code: str
    length_meters: int
    surface_type: str

class Aircraft(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    registration: str
    icao_type: str
    manufacturer: str
    model: str
    operator: str
    status: str
    flights: List["Flight"] = Relationship(back_populates="aircraft")

class AircraftCreate(BaseModel):
    registration: str
    icao_type: str
    manufacturer: str
    model: str
    operator: str
    status: str

class AircraftUpdate(BaseModel):
    operator: str
    status: str

class AircraftResponse(BaseModel):
    id: int
    registration: str
    icao_type: str
    manufacturer: str
    model: str
    operator: str
    status: str

class Flight(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    flight_number: str
    aircraft_id: int = Field(foreign_key="aircraft.id")
    departure_airport_id: int = Field(foreign_key="airport.id")
    arrival_airport_id: int = Field(foreign_key="airport.id")
    scheduled_departure: datetime
    scheduled_arrival: datetime
    status: str
    aircraft: Optional["Aircraft"] = Relationship(back_populates="flights")
    departure_airport: Optional["Airport"] = Relationship(
        sa_relationship_kwargs={"foreign_keys": "[Flight.departure_airport_id]"}
    )
    arrival_airport: Optional["Airport"] = Relationship(
        sa_relationship_kwargs={"foreign_keys": "[Flight.arrival_airport_id]"}
    )

class FlightCreate(BaseModel):
    flight_number: str
    aircraft_id: int
    departure_airport_id: int
    arrival_airport_id: int
    scheduled_departure: datetime
    scheduled_arrival: datetime
    status: str

class FlightUpdate(BaseModel):
    scheduled_departure: datetime
    scheduled_arrival: datetime
    status: str

class FlightResponse(BaseModel):
    id: int
    flight_number: str
    aircraft_id: int
    departure_airport_id: int
    arrival_airport_id: int
    scheduled_departure: datetime
    scheduled_arrival: datetime
    status: str

class FlightDetailedResponse(BaseModel):
    flight_number: str
    aircraft: AircraftResponse
    departure_airport: AirportResponse
    arrival_airport: AirportResponse

