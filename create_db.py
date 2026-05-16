import sqlite3
import random
from datetime import datetime, timedelta

# Create database
conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

# Create sales table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id        INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME,
        product   TEXT,
        quantity  INTEGER,
        revenue   REAL,
        region    TEXT
    )
''')

# Products and regions
products = ['Laptop', 'Phone', 'Tablet', 'Watch', 'Headphones']
regions  = ['North', 'South', 'East', 'West']

# Generate 90 days of fake sales data
start_date = datetime.now() - timedelta(days=90)

for i in range(500):
    timestamp = start_date + timedelta(
        days=random.randint(0, 90),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59)
    )
    product  = random.choice(products)
    quantity = random.randint(1, 10)
    revenue  = round(random.uniform(100, 5000), 2)
    region   = random.choice(regions)

    cursor.execute('''
        INSERT INTO sales
        (timestamp, product, quantity, revenue, region)
        VALUES (?, ?, ?, ?, ?)
    ''', (timestamp, product, quantity, revenue, region))

conn.commit()
conn.close()
print("✅ sales.db created with 500 records!")