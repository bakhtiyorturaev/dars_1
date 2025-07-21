class Car:
    def __init__(self, name, model, kompany, year):
        self.name = name
        self.model = model
        self.kompany = kompany
        self.year = year

    @property
    def get_info(self):
        return self.name#, self.model, self.kompany, self.year

    @get_info.setter
    def get_info(self):
        return self.name



obj1 = Car('Cobalt', 'avtomat', 'chevorolet', 2025)
obj2 = Car('Cobalt', 'avtomat', 'chevorolet', 2025)

# print(obj1 == obj2)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


x = Person('Mike', 25)
y = Person('Sarah', 27)
z = Person('Mike', 25)

print(x == z)



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return 'ikkalasi teng'
        else:
            'teng emas'
            return None

    # def __del__(self):
    #     print(self.name, 'ochrildi')

    # def __lt__(self, age):
    #     return 'Haa'

    # def __gt__(self, name):
    #     return 'Haa'

x = Person('Mike', 25)
y = Person('Sarah', 27)
z = Person('Mike', 25)

# print(x == z)

print(x > y)
