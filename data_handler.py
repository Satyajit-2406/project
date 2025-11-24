import csv
import os
from datetime import datetime

# Configuration
CSV_PATH = 'data/transactions.csv'
COLUMN_NAMES = ['ID', 'Date', 'Type', 'Category', 'Amount', 'Description']

def read_transactions():
    """Read all financial records from storage"""
    if not os.path.exists(CSV_PATH):
        print(f"No existing file found. Setting up new database at {CSV_PATH}")
        os.makedirs('data', exist_ok=True)
        write_transactions([])
        return []
    
    try:
        records = []
        with open(CSV_PATH, 'r', newline='') as csvfile:
            data_reader = csv.DictReader(csvfile)
            for row in data_reader:
                records.append(row)
        return records
    except IOError as err:
        print(f"Problem reading file: {err}")
        return []

def write_transactions(records):
    """Write transaction records back to storage"""
    try:
        with open(CSV_PATH, 'w', newline='') as csvfile:
            data_writer = csv.DictWriter(csvfile, fieldnames=COLUMN_NAMES)
            data_writer.writeheader()
            for record in records:
                data_writer.writerow(record)
    except IOError as err:
        print(f"Couldn't save to file: {err}")
        