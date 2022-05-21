import psycopg2
from psycopg2 import Error

connection = psycopg2.connect(user="r", password="123456", host="127.0.0.1", port="5532", database="BD")

cursor = connection.cursor()
postgreSQL_select_Query = "SELECT * FROM test_db"
cursor.execute(postgreSQL_select_Query)
date = cursor.fetchall()

for row in date:
 print(row[0], row[1], row[2], row[3])

connection: cursor.close()
connection.close()
