import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from db.models import Customer, Reservation, Table

import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Customer, Reservation, Table
from datetime import datetime

# Database setup
engine = create_engine('sqlite:///restaurant_reservation.db')
Session = sessionmaker(bind=engine)
session = Session()

# Menu display
def display_menu():
    print("==============================")
    print("     Restaurant CLI Menu       ")
    print("==============================")
    print("1. Create a customer")
    print("2. Update a customer")
    print("3. Delete a customer")
    print("4. Create a reservation")
    print("5. View reservations")
    print("6. Cancel a reservation")
    print("7. View available tables")
    print("8. Exit")
    print("==============================")

def create_customer():
    name = input("Enter customer name: ")
    phone = input("Enter customer phone: ")
    customer = Customer(name=name, phone=phone)
    session.add(customer)
    session.commit()
    print(f"Customer '{name}' added successfully.")

def update_customer():
    customer_id = input("Enter customer ID to update: ")
    customer = session.query(Customer).filter_by(id=customer_id).first()
    if customer:
        name = input(f"Enter new name for {customer.name} (leave blank to keep current): ") or customer.name
        phone = input(f"Enter new phone for {customer.phone} (leave blank to keep current): ") or customer.phone
        customer.name = name
        customer.phone = phone
        session.commit()
        print("Customer details updated.")
    else:
        print(f"Customer with ID {customer_id} not found.")

def delete_customer():
    customer_id = input("Enter customer ID to delete: ")
    customer = session.query(Customer).filter_by(id=customer_id).first()
    if customer:
        session.delete(customer)
        session.commit()
        print(f"Customer '{customer.name}' deleted.")
    else:
        print(f"Customer with ID {customer_id} not found.")

def create_reservation():
    customer_id = input("Enter customer ID: ")
    table_id = input("Enter table ID: ")
    date_str = input("Enter reservation date (YYYY-MM-DD): ")
    reservation_date = datetime.strptime(date_str, '%Y-%m-%d')
    reservation = Reservation(customer_id=customer_id, table_id=table_id, date=reservation_date)
    session.add(reservation)
    session.commit()
    print("Reservation created successfully.")

def view_reservations():
    reservations = session.query(Reservation).all()
    if reservations:
        for res in reservations:
            print(f"Reservation {res.id}: Customer {res.customer_id}, Table {res.table_id}, Date {res.date}")
    else:
        print("No reservations found.")

def cancel_reservation():
    res_id = input("Enter reservation ID to cancel: ")
    reservation = session.query(Reservation).filter_by(id=res_id).first()
    if reservation:
        session.delete(reservation)
        session.commit()
        print(f"Reservation {res_id} canceled.")
    else:
        print(f"Reservation with ID {res_id} not found.")

def view_tables():
    tables = session.query(Table).all()
    for table in tables:
        print(f"Table {table.id}: Capacity {table.capacity}")

def main():
    while True:
        display_menu()
        choice = input("Enter the number of your choice: ")
        if choice == '1':
            create_customer()
        elif choice == '2':
            update_customer()
        elif choice == '3':
            delete_customer()
        elif choice == '4':
            create_reservation()
        elif choice == '5':
            view_reservations()
        elif choice == '6':
            cancel_reservation()
        elif choice == '7':
            view_tables()
        elif choice == '8':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
