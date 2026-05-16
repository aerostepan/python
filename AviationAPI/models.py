from pydantic import BaseModel

class Airport(BaseModel):
    icao: str
    iata: str
    name: str
    city: str
    country: str


