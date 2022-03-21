# Static Method & Class Method

"""  
    Waktu Kegunaan Static Method :
    1. dapat digunakan tanpa instansi ke object terlebih dahulu
    2. digunakan untuk membuat fungsi utilitas pada class
    3. digunakan ketika mengumpulkan berbagai fungsi sejenis ke dalam class
    4. digunakan ketika ingin fungsi tidak ditimpa class turunan

    Waktu Kegunaan Class Method :
    1. Untuk fungsi-fungsi yang berkaitan secara langsung dengan instance variable, gunakan instance method.
    2. Untuk fungsi-fungsi yang bersifat utilitas (helper/bantuan) dan tidak berkaitan secara langsung dengan instance variable, gunakanlah static method.
    3. Dan untuk membuat factory method (hampir sama seperti konstruktor dengan use case berbeda), kita bisa menggunakan class method
"""

class Hero :
    # private class variable
    __jumlah = 0

    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1

    # method hanya berlaku untuk object
    def getJumlah(self) :
        return Hero.__jumlah

    # method hanya berlaku untuk class
    def getJumlah1() :
        return Hero.__jumlah
    
    # static method
    @staticmethod
    def getJumlah2() : 
        return Hero.__jumlah

    # class method ~ wajib memberi 1 parameter untuk mengarah ke class
    @classmethod
    def getJumlah3(cls) :
        return cls.__jumlah

yuko = Hero("Yuko")
dexter = Hero("Dexter")
jack = Hero("Jack")

# print(Hero.getJumlah()) # error karena methodnya hanya untuk object
# print(yuko.getJumlah()) # ini baru bisa untuk object yuko

# print(yuko.getJumlah1()) # ini error karena methodnya hanya untuk class
# print(Hero.getJumlah1()) # ini baru bisa untuk class

# keduanya bisa menampilkan jumlah, karena static method
# print(yuko.getJumlah2())
# print(Hero.getJumlah2())

print(yuko.getJumlah3())
print(Hero.getJumlah3())