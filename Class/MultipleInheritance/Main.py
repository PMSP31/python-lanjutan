# Multiple Inheritance

class A :
    # method resolution order ~ urutan eksekusi method pada multiple inheritance
    # def method_A(self):
    def show(self):
        print("ini method a")
    
class B :
    # def method_B(self):
    def show(self):
        print("ini method b")

# inheritance biasa
# class C(A) :

# Multiple Inheritance
class C (A, B):
    pass

obj = C()

# obj bisa menggunakan semua method dari multiple inheritance
# obj.method_A()
# obj.method_B()

obj.show()
# help(obj)
# urutan eksekusi method
# C - B - A