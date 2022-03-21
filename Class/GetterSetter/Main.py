# Getter & Setter

class Hero :
    def __init__(self, name, health, armor) :
        self.__name = name
        self.__health = health
        self.__armor = armor

    # mengubah method menjadi property
    @property
    def info(self) : 
        return f"name {self.__name} : \n\tHealth : {self.__health}"

    # getter standar dari paradigma OOP biasa
    def getName(self) :
        return self.__name

    # setter standar
    def setName(self, newName) :
        self.__name = newName

    @property
    def armor(self) :
        pass

    # getter oop python
    @armor.getter
    def armor(self) :
        return self.__armor

    # setter oop python
    @armor.setter
    def armor(self, newArmor) :
        self.__armor = newArmor

    # deleter ~ digunakan untuk menghapus property
    @armor.deleter
    def armor(self) :
        print("Armor kosong!")
        self.__armor = None

jito = Hero("Jito", 100, 50)

# print(jito.info)

# kemudahan saat menggunakan getter & setter dari Python
print(jito.armor)
jito.armor = 78
print(jito.armor)

del jito.armor
print(jito.__dict__)