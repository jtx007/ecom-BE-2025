# FastAPI Backend with SQLAlchemy and PostgreSQL

A modern backend API built with FastAPI, SQLAlchemy ORM, and PostgreSQL database.

## Features

- FastAPI for high-performance API development
- SQLAlchemy ORM for database operations
- PostgreSQL as the database
- JWT Authentication
- User registration and login
- Environment variable configuration
- CORS middleware
- Pydantic models for request/response validation

## Prerequisites

- Python 3.9+
- PostgreSQL
- pip (Python package manager)

## Setup

1. Clone the repository:

```bash
git clone <your-repo-url>
cd <your-repo-name>
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a PostgreSQL database named `tba_db`

5. Copy the `.env.example` file to `.env` and update the values:

```bash
cp .env.example .env
```

6. Update the database URL in `.env` if needed:

```
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/tba_db
```

7. Start the application:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the application is running, you can access:

- Interactive API documentation: `http://localhost:8000/docs`
- Alternative API documentation: `http://localhost:8000/redoc`

## API Endpoints

- `POST /api/v1/login` - User login
- `POST /api/v1/users` - Create new user
- `GET /api/v1/users/me` - Get current user info

## Authentication

The API uses JWT tokens for authentication. To authenticate:

1. Get a token by sending a POST request to `/api/v1/login` with your credentials
2. Include the token in the Authorization header of subsequent requests:

   ```
   Authorization: Bearer <your-token>
   ```
# ecom-BE-2025
