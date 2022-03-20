# Latihan OOP 1

from math import ceil


class Hero :
    def __init__(self, name, health, attackPower, armor) :
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armor = armor

    def attack(self, enemy) :
        print(f"{self.name} attack {enemy.name}")
        enemy.attacked(self)

    def attacked(self, enemy):
        print(f"{self.name} has been attacked by {enemy.name}")
        enemyDamage = enemy.attackPower / self.armor
        print(f"Damage received : {str(enemyDamage)}")
        self.health -= enemyDamage
        print(f"{self.name} health remaining {str(ceil(self.health))}")

octane = Hero("Octane", 100, 12, 25)
bloodhound = Hero("BloodHound", 100, 5, 50)

while True : 
    octane.attack(bloodhound)
    print('\n')
    bloodhound.attack(octane)

    if octane.health < 0 :
        print("== Octane Death ==\n")
        print("Bloodhound Win The Game!!")
        break
    elif bloodhound.health < 0 :
        print("== Bloodhound Death ==\n")
        print("Octane Win The Game!!")
        break