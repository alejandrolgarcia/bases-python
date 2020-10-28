import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="8889",
  user="root",
  password="root",
  database="mydb_python"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydb_python")
# mycursor.execute("SHOW DATABASES")

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")