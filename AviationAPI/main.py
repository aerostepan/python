from fastapi import FastAPI
from routes.airports import router as airports_router
from routes.runways import router as runways_router
from routes.aircrafts import router as aircrafts_router
from database.db import create_db_and_tables

app = FastAPI()
app.include_router(airports_router)
app.include_router(runways_router)

app.include_router(aircrafts_router)

create_db_and_tables()
