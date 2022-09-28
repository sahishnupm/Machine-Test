import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

mycursor = db.cursor()
cursor2 = db.cursor()
