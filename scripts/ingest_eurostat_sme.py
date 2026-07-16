#ingest the dataset into sql db 
import csv
import sqlite3
 # Connecting to the database
con = sqlite3.connect('sme_research.db')
msg = "connection check!"
print(msg)

# Creating a cursor object to execute
# SQL queries on a database table
cur = con.cursor()
msg2 = "cursor check!"
print(msg2)

# Table Definition
create_table = '''CREATE TABLE sme_by_sector
                (
                id INTEGER PRIMARY KEY AUTOINCREMENT
                );
                '''