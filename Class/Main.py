# Class pada python

# Class adalah object constructor / blueprint untuk membuat object

# membuat class
class Coba : 
    x = 5
# mengambil data pada class
print(Coba.x)

# __init__()
# __init__() digunakan untuk menetapkan nilai ke properti objek, atau operasi lain yang perlu dilakukan saat objek sedang dibuat:
class Person :
    def __init__(self, name, age) : # self pada parameter digunakan untuk mengakses variable milik kelas
        # nama nya tidak harus self, tetapi wajib menjadi parameter pertama!!
        self.name = name
        self.age = age

    def salam(self) : 
        print(f"Hello nama saya {self.name}")

p1 = Person("Paul", 17)
# print(p1) # p1 adalah object dari Class Person
print(p1.name)
print(p1.age)
p1.salam()

# mengganti properties object
p1.age = 18
print(p1.age)

# menghapus propertiess ~ del
del p1.age
# print(p1.age) # akan error

# menghapus object
del p1
# print(p1)