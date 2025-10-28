import pyodbc
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=Arian;'
    'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute("select * from school_data")
for row in cursor.fetchall():
    print(row)

import pyodbc
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=Arian;'
    'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute("""insert into Arian (id, name, class, mark, gender) values (?, ?, ?, ?, ?, ?)
""")
for row in cursor.fetchall():
    print(row)
'___________________________________________________________________________________________________'
import pymongo
from pymongo import MongoClient
conn = pymongo.MongoClient(host = 'localhost', port = 27017)
db = conn['Arian']
col = db['test collection']
col.insert_one({'_id': int, 'name': str, 'class':str, 'mark': int, 'gender': str})
