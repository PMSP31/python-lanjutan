# import module
import mysql.connector

# connection DB
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "python_mysql"
)

mycursor = conn.cursor()

# create Table
# mycursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255))")

# Alter table
mycursor.execute("ALTER TABLE `users` ADD `user_id` INT NOT NULL AUTO_INCREMENT FIRST, ADD PRIMARY KEY (`user_id`);")

# show all Tables
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)