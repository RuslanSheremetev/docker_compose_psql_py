import psycopg2
from psycopg2 import Error

connection = psycopg2.connect(user="r", password="123456", host="127.0.0.1", port="5532", database="BD")

cursor = connection.cursor()

insert_query = """ INSERT INTO test_db (ID, First_name, Second_name, Data_of_birth) VALUES
                                          (2, 'Ruslan', 'Sheremetev', '1990-11-09')"""
cursor.execute(insert_query)
connection.commit()
connection: cursor.close()
connection.close()
