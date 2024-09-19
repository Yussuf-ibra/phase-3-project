from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)

    reservations = relationship("Reservation", back_populates="customer")

class Table(Base):
    __tablename__ = 'tables'
    
    id = Column(Integer, primary_key=True)
    capacity = Column(Integer)

    reservations = relationship("Reservation", back_populates="table")

class Reservation(Base):
    __tablename__ = 'reservations'
    
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    table_id = Column(Integer, ForeignKey('tables.id'))
    date = Column(DateTime)

    customer = relationship("Customer", back_populates="reservations")
    table = relationship("Table", back_populates="reservations")

# Database connection
engine = create_engine('sqlite:///restaurant_reservation.db')
Base.metadata.create_all(engine)
