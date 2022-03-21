# Latihan Inheritance
from Hero import *

jack = HeroFighter("Jack")
bob = HeroTank("Bob")
jack.showInfo()
bob.showInfo()

jack.gainExp = 200
bob.gainExp = 250

jack.showInfo()
bob.showInfo()