import os
import datetime
import pymysql

# Get the username from the Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    with connection.cursor() as cursor:
        rows = [("Bob", 21, "1990-02-06 23:04:56"),
               ("Prick", 2, "1991-03-07 23:04:56"),
               ("Knob", 1, "1992-04-08 23:04:56"),
               ("Fag", 210, "1993-05-09 23:04:56")]
        cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", rows)
        connection.commit()
finally:
    connection.close()