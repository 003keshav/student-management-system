import os
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("DB_PASSWORD"),
    database="Student_db"
)
cursor=conn.cursor()