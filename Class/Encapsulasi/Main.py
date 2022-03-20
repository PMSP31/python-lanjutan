# Encapsulasi ~ membuat semua variable menjadi private
# untuk mengakses variable private, diperlukan getter & setter
class Hero :
    def __init__(self, name, health, attackPower) :
        self.__name = name
        self.__health = health
        self.__attackPower = attackPower

    # getter
    def getName(self) :
        return self.__name

    # setter
    def setName(self, newName) :
        self.__name = newName

wesly = Hero("wesly", 88, 34)

# mengakses name
# print(wesly.__name) # ini akan error, karena tidak bisa mengakses private variable diluar class
print(wesly.getName()) # ini baru bisa

# mengubah name
# wesly.__name = "Wesly" # ini tetap saja tidak berubah
wesly.setName("Wesly") # ini baru bisa
print(wesly.getName())