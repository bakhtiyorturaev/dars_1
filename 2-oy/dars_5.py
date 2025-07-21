# Polimorfizm – bu bir xil nomdagi metod yoki funksiyaning har xil klasslarda turlicha ishlashi.

# Overriding – bu ota (super) klassdagi metodni voris (child) klassda o‘zgartirib yozish.
    #maqsad:
    # – Klassni moslashtirish
    # – Ota klassdagi metodni xohlaganingizcha yangilash

# Overloading – bu bir xil nomdagi metod/funksiyani har xil argumentlar bilan ishlatish.
    # Python’da haqiqiy method overloading to‘liq qo‘llab-quvvatlanmaydi,
    # lekin *args, **kwargs orqali shunga o‘xshash effektga erishish mumkin.


# - encapculation
# public, _protect, __pravite,
# getter, setter
# overriding, overloading


# class Person:
#     def __init__(self, name, shahri, tyili):
#         self.name = name
#         self.shahri = shahri
#         self.tyili = tyili
#
#     def get_age(self):
#         return 2025 - self.tyili, self.name
#
#
# class Dasturchi(Person):
#     def __init__(self, name, shahri, tyili, company, prof):
#         super().__init__(name, shahri, tyili)
#         self.company = company
#         self.prof = prof
#
#     def get_age(self):
#         return 2025 - self.tyili
#
#
# dasturchi = Dasturchi('Islom', 'Toshkent', 2006, 'Google', 'Python')
# dasturchi2 = Person('Baxtiyor', 'Surxondaryo vil', 2001)
#
# print(dasturchi2.get_age())familiya


# - encapculation
# public, _protect, __pravite,
# getter, setter

class Bank:
    def __init__(self, name, balance, card_number):
        self.name = name  # public atribut
        self._card_number = card_number # protect
        self.__balance = balance # public

    def __get_info(self):
        return self.name, self._card_number, self.__balance

    def get_balance(self):
        return self.__balance



bank = Bank('Ipak yo\'li', 100, 73276253)
# print(bank.get_info())
# print(bank.__balance)
# print(bank.name)
# print(bank.get_balance())

class Mijoz(Bank):
    def __init__(self, name, balance, card_number, familiya):
        super().__init__(name, balance, card_number)
        self.familiya = familiya

    def __get_info(self):
        return self.name, self._card_number

    def _get_info(self):
        return self.name, self._card_number

mijoz = Mijoz('Baxtiyor', 100, 32857438, "To'rayev")

# print(mijoz._get_info())


class Talaba:
    def __init__(self, name, yoshi, id):
        self.name = name
        self._yoshi = yoshi
        self.__id = id

        #getter
    def get_yosh(self):
        return self._yoshi

        #setter
    def set_yosh(self, a):
        if a < 0:
            return 'minus son kiritish mumkin emas'
        else:
            return self._yoshi + a

talaba = Talaba('Baxtiyor', 24, 5)

print(talaba.get_yosh())
print(talaba.set_yosh(20))
print(talaba._yoshi)