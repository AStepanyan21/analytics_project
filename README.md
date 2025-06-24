
# Analytics Project

A simple product analytics service with data parsing from Wildberries, REST API, and React frontend embedded in Django templates.

---

## Project Overview

- Parses product data from Wildberries based on user search queries.
- Stores product info in PostgreSQL database.
- Provides REST API with filtering and pagination.
- React frontend with product table and interactive charts.
- Dockerized environment for easy setup and deployment.

---

## Technologies

- Python 3.11, Django 4.x, Django REST Framework
- PostgreSQL
- Poetry for dependency management
- React + Vite (embedded in Django templates)
- Docker & Docker Compose

---

## Quick Start (Local Development)

### Clone the repository

```bash
git clone https://github.com/AStepanyan21/analytics_project
cd analytics_project
```

### Install dependencies

```bash
poetry install
```

### Setup environment variables

Create a `.env` file in the project root with the following content:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=your_db
DB_USER=your_db_user
DB_PASSWORD=your_db_pass
DB_HOST=localhost
DB_PORT=5432
```

### Apply database migrations

```bash
poetry run python manage.py migrate
```

### Run the development server

```bash
poetry run python manage.py runserver
```

---

## Running the Wildberries parser

To fetch product data asynchronously from Wildberries, run:

```bash
poetry run python manage.py parse_wb_async <query> --pages <number_of_pages>
```

Example:

```bash
poetry run python manage.py parse_wb_async laptop --pages 3
```

---

## Running tests

Run the test suite with:

```bash
poetry run pytest
```

---

## Running with Docker Compose

### Build and start containers

```bash
docker-compose up --build
```

### Run database migrations inside the container

In a new terminal window, run:

```bash
docker-compose exec web python manage.py migrate
```

### Run the Wildberries parser inside the container

```bash
docker-compose exec web python manage.py parse_wb_async laptop --pages 3
```



