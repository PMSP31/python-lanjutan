# Scope pada Python

# Local Scope
# variable yang hanya bisa digunakan pada scope function itu sendiri
def myFunc() : 
    x = 10
    print(f"local scope : {x}")

myFunc()
# print(x) # ini akan error, karena variable pada local scope tidak bisa digunakan diluar scope / diluar functionnya

# local scope untuk function dalam function
def mFunc() :
    x = 20
    def innerFunc() :
        print(f"inner function menggunakan variable local : {x}") # ini bisa digunakan, karena function ini berada didalam local scope
    innerFunc()

mFunc()

# Global Scope vs Local Scope

x = 100 # ini variable global scope

def my_func() :
    print(f"mengambil variable dari global scope ke function : {x}") # kita dapat mengambil global variable

my_func()
print(x)

# penamaan variable
x = 50

def my_Func() :
    x = 200
    print(f"ini dari local scope : {x}") # ini akan mengambil dari local scope terlebih dahulu

my_Func()
print(f"ini dari global scope : {x}") # ini langsung mengambil dari global

""" urutan pengecekan variable pada function
    - varible dalam function / variable local scope
    - dari parameter
    - baru ke global scope
"""

# global Keyword ~ digunakan untuk membuat global variable
def m_func() :
    global x
    x = 400

m_func()
print(f"ini dari keyword global : {x}")

# mengubah value varible global, menggunakan keyword global
x = 120
print(f"ini sebelum diubah dari keyword : {x}")

def myFunc() :
    global x 
    x = 500

myFunc()
print(f"ini setelah diubah dengan keyword : {x}")