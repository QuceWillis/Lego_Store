import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123Password"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE Lego")
