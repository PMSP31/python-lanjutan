# Diamond Problem

class A :

    def show(self) :
        print("ini show A")

class B(A) :

    def show(self) :
        print("ini show B")

class C(A) :

    def show(self) :
        print("ini show C")

class D(B, C):
    pass

obj = D()
obj.show()
help(obj)

# urutan eksekusi method inheritance
# D - B - C - A