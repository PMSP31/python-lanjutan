# Abstract Class ~ instance dari abstract class adalah class
# memaksa class turunannya menggunakan abstractmethod

# membuat abstract class
# abc = abstract base class
from abc import ABC, abstractmethod

class Button(ABC) :
    @abstractmethod
    def click (self) : 
        pass

class PushButton(Button) :
    # wajib memiliki method click
    def click(self):
        print("Push Button Click")

class RadioButton(Button):
    def click(self):
        print("Radio Button Click")

button1 = PushButton()
button2 = RadioButton()

button1.click()
button2.click()