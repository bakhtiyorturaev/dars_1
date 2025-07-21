
from abc import ABC, abstractmethod

# Create Abstract base class
class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    # Create abstract method
    @abstractmethod
    def printDetails(self):
        pass

    # Create concrete method
    def accelerate(self):
        print("Speed up ...")

    def break_applied(self):
        print("Car stopped")


# Create a child class
class Hatchback(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

    def sunroof(self):
        print("Not having this feature")


# Create a child class
class Suv(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

    def sunroof(self):
        print("Available")


# Create an instance of the Hatchback class
car1 = Hatchback("Maruti", "Alto", "2022")

object = Suv('merc', 'merc 23', 2024)
# print(object.printDetails())

# Call methods
# car1.printDetails()
# car1.accelerate()
# car1.sunroof()




from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(yosh):
        return yosh > 18


person1 = Person('mayank', 21)

person2 = Person.fromBirthYear('mayank', 1996)

# print(person1.age)
# print(person2.age)

# print the result
# print(Person.isAdult(22))
