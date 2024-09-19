import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Table

# Database setup
engine = create_engine('sqlite:///restaurant_reservation.db')
Session = sessionmaker(bind=engine)
session = Session()

# Seed the database with tables
tables = [
    Table(capacity=2),
    Table(capacity=4),
    Table(capacity=6),
    Table(capacity=8)
]

session.add_all(tables)
session.commit()

print("Tables seeded successfully.")
