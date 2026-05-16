from fastapi import FastAPI
from routes.airports import router as airports_router

app = FastAPI()
app.include_router(airports_router)
