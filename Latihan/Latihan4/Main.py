# Latihan Python MySQL

import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'python_mysql'
)

mycursor = conn.cursor()

mycursor.execute("SELECT * from users")

result = mycursor.fetchall()

print(20*"=", " Data User ", 20*"=")
for user in result :
    print(f"\nID\t : {user[0]}")
    print(f"Name\t : {user[1]}")
    print(f"Email\t : {user[2]}")
    
print("\n")
print(55*"=")

option = input("Do you want to add new user ? (Y/N) : ").lower()

if option == "y" :
    # get data by input
    name = str(input("input your name : "))
    email = str(input("input your email : "))

    # insert data
    sql = "INSERT INTO users (user_id, name, email) VALUES (null, %s, %s)"
    val = (name, email)

    # try-except 
    try:
        mycursor.execute(sql, val)
    except:
        # if error
        print("\nSomething went wrong")
    else:
        # if not error, commit / push data
        conn.commit()
        print("\nNEW DATA ADDED.")
        
elif option == "n" :
    pass
else :
    print("\nINVALID INPUT !!!")

print("\nThanks for use the program!")