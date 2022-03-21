# Latihan Encapsulasi

class Hero :
    # private class variable
    __jumlah = 0

    def __init__(self, name, health, attPower, armor) : 
        self.__name = name
        self.__healthBase = health
        self.__attPowerBase = attPower
        self.__armorBase = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthBase * self.__level
        self.__attPower = self.__attPowerBase * self.__level
        self.__armor = self.__armorBase * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self) :
        return f"""
        {self.__name} ({self.__level}) :
            Health = {self.__health} / {self.__healthMax}
            Attack = {self.__attPower}
            Armor  = {self.__armor}"""

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp) :
        self.__exp += addExp
        if(self.__exp >= 100) :
            print(f"\n{self.__name} LEVEL UP !!")
            print(self.info)
            self.__level += 1
            self.__exp -= 100
            
            self.__healthMax = self.__healthBase * self.__level
            self.__attPower = self.__attPowerBase * self.__level
            self.__armor = self.__armorBase * self.__level

    def farming(self) :
        self.gainExp = 20

jumper = Hero("Jumper", 100, 45, 75)

print(jumper.info)

for i in range(21) :
    jumper.farming()