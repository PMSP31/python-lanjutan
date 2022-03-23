# import module
import mysql.connector

# connection DB
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

mycursor = conn.cursor()

# create DB
# mycursor.execute("Create Database python_mysql") 
# jika dijalankan kembali akan error

# show all DB
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)