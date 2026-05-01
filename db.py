import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="Student_db"
)
cursor=conn.cursor()