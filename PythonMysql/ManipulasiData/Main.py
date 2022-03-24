import mysql.connector

# connection DB
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "python_mysql"
)

mycursor = conn.cursor()

# insert single
""" sql = "INSERT INTO users (user_id, name, email) VALUES (null, %s, %s)"
val = ("John", "john@gmail.com")
mycursor.execute(sql, val) """

# insert multiple
""" sql = "INSERT INTO users (user_id, name, email) VALUES (null, %s, %s)"
val = [
        ("Doe", "doe@gmail.com"),
        ("Rio", "rio@gmail.com"),
        ("Dave", "dave@gmail.com"),
        ("Jason", "jason@gmail.com"),
        ("Sonya", "sonya@gmail.com")
    ] """

# untuk eksekusi banyak data
# mycursor.executemany(sql, val)

# digunakan untuk mengirim data
# conn.commit()

# select 
# mycursor.execute("SELECT * FROM users")
# mycursor.execute("SELECT name FROM users")

# fetch all rows
# result = mycursor.fetchall()

# fetch one rows
# result = mycursor.fetchone()
# print(result)

# for x in result:
#     print(x)

# show record inserted
# print(mycursor.rowcount, "record inserted.")
# show lastrow inserted id
# print("1 record inserted, ID:", mycursor.lastrowid)

# where
# sql = "SELECT * FROM users WHERE name = 'Doe' "

# LIKE
# sql = "SELECT * FROM users WHERE name LIKE '%J%' "
# mycursor.execute(sql)

# sql injection ~ %s (escape query values)
# digunakan untuk menghindari SQL Injection
# sql = "SELECT * FROM users WHERE email = %s"
# email = ("sonya@gmail.com",)

# mycursor.execute(sql, email)

# order by ~ default (ASC)
""" sql = "SELECT * FROM users ORDER BY name "
sql = "SELECT * FROM users ORDER BY name DESC"

mycursor.execute(sql)

result = mycursor.fetchall()

for x in result :
    print(x) """

# update
# sql = "UPDATE users SET email = 'johny@gmail.com' WHERE name = 'John'"
# mycursor.execute(sql)

# %s
sql = "UPDATE users SET email = %s WHERE name = %s"
val = ("john@gmail.com", "John")

mycursor.execute(sql, val)

conn.commit()

print(mycursor.rowcount, "record(s) affected")

# delete
# sql = "DELETE FROM users WHERE name = 'Rio'"
# mycursor.execute(sql)

# &s
""" sql = "DELETE FROM users WHERE email = %s"
email = ("doe@gmail.com",)
mycursor.execute(sql, email)

conn.commit()

print(mycursor.rowcount, 'record(s) deleted') """

# drop table
""" sql = "DROP TABLE tes"
# if exists
sql = "DROP TABLE IF EXISTS tes"
mycursor.execute(sql) """
