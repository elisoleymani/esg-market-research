#ingest the dataset into sql db 
import csv
import sqlite3
import pandas as pd

#get path
import os 
cwd = os.getcwd()
print(cwd)
#load the data
df = pd.read_csv('data/raw/sbs_sc_sca_r2defaultview_linear_2_0.csv') 

print(df.shape)
print(df.columns.tolist())
# print(df.head(10))
#print(df.dtypes)

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
df.to_sql('sme_by_sector', con, if_exists='replace', index=False)
print(pd.read_sql("SELECT * FROM sme_by_sector LIMIT 5", con))