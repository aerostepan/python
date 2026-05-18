from fastapi import FastAPI
from routes.airports import router as airports_router
from database.db import create_db_and_tables

app = FastAPI()
app.include_router(airports_router)

create_db_and_tables()
