# AviationAPI

AviationAPI is a FastAPI-based backend project for managing aviation-related operational data.

The project currently supports airport and runway management and is being developed toward an airport operations management system.

The main goal of this project is to practice backend development with Python while building a realistic aviation-related API.

---

## Technologies

- Python
- FastAPI
- SQLModel
- SQLite
- Uvicorn
- Pydantic

---

## Project Architecture

The project uses a layered backend architecture:

```text
ROUTES
↓
SERVICES
↓
REPOSITORY
↓
DATABASE
```

### Routes Layer

Responsible for:

- API endpoints
- HTTP request handling
- HTTP exceptions
- calling service functions

### Service Layer

Responsible for:

- business logic
- validation rules
- checking if entities exist
- preparing response data
- raising business-level errors

### Repository Layer

Responsible for:

- database queries
- insert operations
- update operations
- delete operations
- database session handling

### Database Layer

Responsible for:

- database engine creation
- table creation
- SQLite connection setup

---

## Current Project Structure

```text
AviationAPI/
│
├── database/
│   ├── db.py
│   ├── airport_repo.py
│   ├── runway_repo.py
│   └── aircraft_repo.py
│
├── routes/
│   ├── airports.py
│   ├── runways.py
│   └── aircrafts.py
│
├── services/
│   ├── airport_service.py
│   ├── runway_service.py
│   └── aircraft_service.py
│
├── models.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Implemented Features

### Airports

The airport module currently supports:

- Create airport
- Get all airports
- Get airport by ICAO code
- Update airport data
- Delete airport

### Runways

The runway module currently supports:

- Create runway
- Get all runways
- Get runway by ID
- Update runway data
- Delete runway

### Aircraft

The aircraft module currently supports:

- Create aircraft
- Get all aircraft
- Get aircraft by Registration
- Update aircraft data
- Delete aircraft

---

## Database Models

### Airport

```python
class Airport(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    icao: str
    iata: str
    name: str
    city: str
    country: str
```

### Runway

```python
class Runway(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    airport_id: int = Field(foreign_key="airport.id")
    runway_code: str
    length_meters: int
    surface_type: str
```

---

## API Endpoints

### Airports

| Method | Endpoint | Description |
|---|---|---|
| GET | `/airports` | Get all airports |
| GET | `/airports/{icao}` | Get airport by ICAO code |
| POST | `/airports` | Create a new airport |
| PUT | `/airports/{icao}` | Update airport data |
| DELETE | `/airports/{icao}` | Delete airport |

### Runways

| Method | Endpoint | Description |
|---|---|---|
| GET | `/runways` | Get all runways |
| GET | `/runways/{runway_id}` | Get runway by ID |
| POST | `/runways` | Create a new runway |
| PUT | `/runways/{runway_id}` | Update runway data |
| DELETE | `/runways/{runway_id}` | Delete runway |

---

## Example Airport Request

```json
{
  "icao": "LOWG",
  "iata": "GRZ",
  "name": "Graz Airport",
  "city": "Graz",
  "country": "AT"
}
```

---

## Example Runway Request

```json
{
  "airport_id": 2,
  "runway_code": "08L/26R",
  "length_meters": 3000,
  "surface_type": "Asphalt"
}
```

Another runway example:

```json
{
  "airport_id": 2,
  "runway_code": "17C/35C",
  "length_meters": 3650,
  "surface_type": "Concrete"
}
```

---

## Installation

### 1. Clone the repository

```bash
git clone <repository_url>
cd AviationAPI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

macOS / Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Project

Start the development server:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger UI will be available at:

```text
http://127.0.0.1:8000/docs
```

---

## Database

The project currently uses SQLite.

The database file is created automatically when the application starts.

Current database setup:

```text
SQLite + SQLModel
```

The database engine is configured in:

```text
database/db.py
```

---

## Important Notes

### SQLite ID Behavior

SQLite does not renumber IDs after deletion.

Example:

```text
Existing IDs:
1
2
3
```

If ID `1` is deleted, the remaining rows keep their original IDs:

```text
2
3
```

The next inserted row will receive a new ID instead of reusing the deleted one.

This is correct database behavior because IDs are stable unique identifiers.

---

### Correct SQLModel Save Pattern

When saving or updating objects with SQLModel, the usual order is:

```python
session.commit()
session.refresh(entity)
```

Reason:

- `commit()` saves changes to the database
- `refresh()` reloads the updated entity from the database

This is especially important when the database generates an ID automatically.

---

## Current Relationship

The project currently has this relationship:

```text
Airport → Runway
```

A runway belongs to an airport through:

```python
airport_id: int = Field(foreign_key="airport.id")
```

---

## Development Notes

Route function names should not be the same as service function names.

Correct example:

```python
create_runway_route()
create_runway_service()
```

Incorrect example:

```python
create_runway_service()
```

inside a route file, because it can overwrite the imported service function and cause recursion errors.

---

## Planned Features

Planned future development:

- Aircraft model
- Flight model
- Gate or stand management
- Flight scheduling
- Airport operations logic
- Relationships between airports, runways, aircraft, and flights
- Better validation rules
- Authentication
- PostgreSQL migration
- Docker support
- Deployment to a VPS or cloud platform

---

## Project Goal

The long-term goal is to develop this project into an airport operations management backend.

Possible future modules:

- airport database
- runway management
- gate and stand assignment
- aircraft management
- flight scheduling
- operational status tracking
- dispatch-related validation logic
