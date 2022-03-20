# Private & Protected variable

# untuk private menggunakan double underscore __
# sedangkan protected menggunakan 1 underscore
class Hero :
    # class variable
    jumlah = 0
    __privateJumlah = 0
    _protectedJumlah = 0

    def __init__(self, name, health) :
        self.name = name
        self.health = health

        # private instance variable
        self.__private = "private"
        # protected instance variable
        self._protected = "protected"

trix = Hero("Trix", 95)

# print(trix.__dict__)
# print(trix.__private)
# print(Hero.__privateJumlah)
print(Hero._protectedJumlah)