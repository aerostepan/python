from __future__ import annotations

from pydantic import BaseModel
from sqlmodel import SQLModel, Field

class Airport(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    icao: str = Field(min_length=4, max_length=4)
    iata: str = Field(min_length=3, max_length=3)
    name: str
    city: str
    country: str

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
    id: int | None = Field(default=None, primary_key=True)
    airport_id: int = Field(foreign_key="airport.id")
    runway_code: str
    length_meters: int
    surface_type: str

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
    id: int | None = Field(default=None, primary_key=True)
    registration: str
    icao_type: str
    manufacturer: str
    model: str
    operator: str
    status: str

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

