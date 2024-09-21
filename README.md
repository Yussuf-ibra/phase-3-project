# Restaurant Reservation CLI App

## Description
A command-line application to manage restaurant reservations using **Python**, **SQLAlchemy ORM**, and **Alembic**. Users can create, view, update, and delete restaurants, customers, and reservations.

## Features
- Add, view, update, and delete reservations
- View restaurant and customer details
- Database migrations with Alembic
- Search for reservations

## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/yussufibra/restaurant-reservation-cli.git
   cd restaurant-reservation-cli
2. Install dependencies:
pip install pipenv
pipenv install
3. Initialize the database:
pipenv run python db/seed.py
4. Apply migrations:
pipenv run alembic upgrade head
5. Start the CLI:
pipenv run python lib/cli.py

## Models Overview
Restaurant: id, name, location
Customer: id, name, phone
Reservation: id, restaurant_id, customer_id, reservation_time
# Migrations
Create migration:
pipenv run alembic revision --autogenerate -m "description"
Apply migration:
pipenv run alembic upgrade head
## License
This project is licensed under the MIT License.