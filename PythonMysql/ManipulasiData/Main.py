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
mycursor.execute("SELECT * FROM users")
# mycursor.execute("SELECT name FROM users")

# fetch all rows
# result = mycursor.fetchall()

# fetch one rows
result = mycursor.fetchone()
print(result)

# for x in result:
#     print(x)

# show record inserted
# print(mycursor.rowcount, "record inserted.")
# show lastrow inserted id
# print("1 record inserted, ID:", mycursor.lastrowid)