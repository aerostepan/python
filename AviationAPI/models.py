from pydantic import BaseModel, Field

class Airport(BaseModel):
    icao: str = Field(min_length=4, max_length=4)
    iata: str = Field(min_length=3, max_length=3)
    name: str
    city: str
    country: str

class AirportUpdate(BaseModel):
    name: str
    city: str
    country: str



