# Inheritance pada Class Python
""" 
    Inheritance / Pewarisan memiliki definisi untuk class yang
    mewarisi/menggunakan semua method & properties pada class lain

    Parent Class = base class, class yang akan diwarisi
    Child Class = class turunan, class yang mewarisi class lain
"""

# Parent Class
class Person : 
    def __init__(self, fname, lname) : 
        self.fname = fname
        self.lname = lname

    def printname(self) :
        print(self.fname, self.lname)

    # add method
    def greet(self) :
        print(f"Halo nama saya {self.fname} {self.lname}.")

# Child Class
# class Student mewarisi semua properties dan method dari Class Person
# class Student(Person) :
#     pass  # keyword pass digunakan jika class tidak memiliki properties dan method, karena class tidak boleh kosong!

# x = Student("Paul", "Mahardika")
# x.printname()

class Student(Person) :
    def __init__(self, fname, lname, year):
        # Person.__init__(self, fname, lname)
        super().__init__(fname, lname) # super() = nama Parent Class
        # add properties
        self.age = year
    # Override
    def greet(self) :
        print(f"Halo nama saya {self.fname} {self.lname}, saya berumur {self.age} tahun.")

    

paul = Student("Paul", "Mahardika", 17)
paul.greet()