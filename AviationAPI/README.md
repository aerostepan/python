# Aviation API Project

A FastAPI-based CRUD API for managing airport data.

This project was created to improve backend development skills with Python and FastAPI while learning API architecture, validation, routing, and service-based backend design.

---

## Features

- Create airports
- Get all airports
- Get airport by ICAO
- Update airport information
- Delete airports
- Pydantic data validation
- Layered backend architecture
- Internal ID generation
- REST-style API endpoints

---

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

Planned upgrades:

- SQLite
- SQLModel
- Persistent database storage

---

## Project Structure

```text
routes/
    airports.py          -> API endpoints and HTTP handling

services/
    airport_service.py   -> Business logic

models.py               -> Pydantic models and validation

database.py             -> Temporary in-memory storage

main.py                 -> FastAPI application entry point
```

---

## API Endpoints

### Airports

| Method | Endpoint | Description |
|---|---|---|
| GET | `/airports` | Get all airports |
| GET | `/airports/{icao}` | Get airport by ICAO code |
| POST | `/airports` | Create a new airport |
| PUT | `/airports/{icao}` | Update airport information |
| DELETE | `/airports/{icao}` | Delete airport |

---

## Validation

The API uses Pydantic models for automatic request validation.

Current validation rules:

- ICAO code must contain exactly 4 characters
- IATA code must contain exactly 3 characters
- Airport update requests cannot change ICAO or IATA codes

---

## How to Run

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the virtual environment

macOS / Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn
```

### 4. Run the server

```bash
uvicorn main:app --reload
```

---

## API Documentation

After starting the server, open:

```text
http://127.0.0.1:8000/docs
```

FastAPI automatically generates interactive API documentation using Swagger UI.

---

## Current Storage

The current version uses temporary in-memory storage in `database.py`.

This means that all created airports are lost when the server restarts.

Planned improvement:

- Replace in-memory storage with SQLite and SQLModel.

---

## Future Improvements

- SQLite database integration
- SQLModel ORM
- Aircraft endpoints
- Flight endpoints
- Authentication and authorization
- Docker support
- Deployment to cloud or VPS
