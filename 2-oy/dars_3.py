class Talaba:
    def __init__(self, name, age, familiya, kurs, city, shakli='Kunduzgi'):
        self.ism = name
        self.yosh = age
        self.familiya = familiya
        self.kurs = kurs
        self.shahri = city
        self.shakli = shakli

    def talaba_info(self):
            return f"talaba ismi {self.ism} yoshi {self.yosh}"

    def talaba_tyili(self):
        return f"tug'ilgan yili {2025-self.yosh}"


talab1 = Talaba('Baxtiyor', 24, 'Turaev', 3, 'Surxondaryo')

print(talab1.shakli)
print(talab1.shahri)

print(talab1.talaba_info())
print(talab1.talaba_tyili())












