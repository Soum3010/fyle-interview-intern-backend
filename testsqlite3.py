import sqlite3
import os 
# Connect to the SQLite databaseimport os

# Get the absolute path to the SQLite database file
current_dir = os.path.dirname(__file__)  # Get the directory of the current script
db_path = os.path.join(current_dir, 'core', 'store.sqlite3')  # Construct the path to the database file

# Connect to the SQLite database using the absolute path
con = sqlite3.connect(db_path)

# Create a cursor object
cur = con.cursor()

# Execute a query to retrieve the names of all tables
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch all table names from the cursor
table_names = cur.fetchall()

# Print the table names
for table in table_names:
    table_name = table[0]
    print(f"Table: {table_name}")
    
    # Fetch all rows from the current table
    cur.execute(f"SELECT * FROM {table_name};")
    rows = cur.fetchall()
    
    # Print the rows
    for row in rows:
        print(row)
    print("\n")

# Close the connection
con.close()
