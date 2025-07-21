# - faker
# - os va pathlib moduli, mkdir(), rmdir(), rename(), remove().
# - random
# from faker import Faker
# fake = Faker(['uz_UZ'])
#
#
# with open('papka/test_uchun.txt', 'w') as file:
#     for _ in range(11):
#         a = file.write(f'{fake.phone_number()}\n')

# with open('sqb.jpg', 'r') as rasm:
#
#     b = rasm.read()
#     with open('a.jpg', 'w') as rasm2:
#         rasm2.write(b)


import os

# os.mkdir('/home/baxti/Desktop/dars/salom')

# print(os.getcwd())

# os.chdir('/home/baxtiyor/dars2')

# print(os.listdir())
# os.remove('a.jpg')




# from pathlib import Path
# #
# p = Path('/')
# #
# for subdir in p.iterdir():
#     if subdir.is_dir():
#         print(subdir)
#
#
#
# sp = p / '/home/baxti/Desktop/dars/example.txt'
# print(sp)










# from faker import Faker
#
# fake = Faker()
#
# print(fake.name())          # Soxta ism
# print(fake.email())         # Soxta email
# print(fake.phone_number())  # Soxta telefon
# print(fake.address())       # Soxta manzil
# print(fake.date_of_birth()) # Tug‘ilgan sana

# for _ in range(5):
#     print({
#         "name": fake.name(),
#         "email": fake.email(),
#         "phone": fake.phone_number()
#     })


# import os
#
# os.mkdir("test_folder")  # test_folder nomli yangi papka yaratadi


# from pathlib import Path
#
# Path("test_folder").mkdir(exist_ok=True)

# os.rmdir("test_folder")
# Path("test_folder").rmdir()
# os.rename("old_name.txt", "new_name.txt")
# Path("old_name.txt").rename("new_name.txt")
# os.remove("file.txt")
# Path("file.txt").unlink()
# path = Path("file.txt")
# if path.exists():
#     print("Fayl mavjud")
# else:
#     print("Fayl yo'q")


# import random
#
# print(random.randint(1, 100))      # 1 va 100 oralig‘ida butun son
# print(random.uniform(1.5, 5.5))    # 1.5 va 5.5 oralig‘ida suzuvchi son

# names = ['Ali', 'Vali', 'Gulbahor', 'Aziza']
# print(random.choice(names))       # Bitta tasodifiy ism
# print(random.sample(names, 2))    # 2 ta tasodifiy ism

# random.shuffle(names)
# print(names)

# print(random.choice([True, False]))



import random

# for _ in range(15):
    # print(random.randint(1, 100))
    # print(random.choice([1, 3, 4, 5, 6,]))
# print(random.choices(1, 3, 4, 5, 6,))












# a = random.randint(50, 100)
# b = random.choice(['Baxtiyor', 'Shaxriyor', 'Islom'])
# c = random.randrange(0, 100)
# print(a)
# print(b)
# print(c)

# def son():
#     dastur_soni = random.randint(1, 100)
#     s = 0
#     while True:
#         s += 1
#         a = int(input('son kiriting '))
#         if a == dastur_soni:
#             break
#         elif a > dastur_soni:
#             print("dastur o'ylagan son kichik")
#         else:
#             print('dastur o\'ylagan son katta')
#     return print(f"{s} ta urinishda topdingiz")
#
# son()

# 1.faker va random orqali ism va yosh generatsiya qilib test1.txt filega "Falonchiyev Pistonchi 23" korinishida har bir qatorda yoziladi.
# o’sha text1.txt faylidagi malumotlarni yosh boyicha sort qilib test2.txt fayliga yosin
# 2. Tepada text1.txt faylidagi Familiyalar bosh harfiga nisbatan alfabit tartibida chiqarsin
# 3.Tepada text1.txt faylidagi yoshi 20 dan kattalarni text3.txt faylida chiqarsin
# 4. Fileda sonlar berilgan tub sonlarni boshqa filega chiqaring
# 5.Fileda sonlar berilgan har bir qatordagi eng katta sonni chiqarib bering
# 6.Fileda sozlar berilgan har bir sozni necha marta qatnashganini chiqarsin
# 5.Fileda matn berilgan matnda eng kop qatnashgan harfni chiqaring.
# 7.FIledagi matnni teskari tartinda chiqaring
# 8.Fileda matn berilgan eng uzun gapni boshqa bir filega chiqaring
# 9.Ikkita fileni malumotlarini birlashtirib chiqaruvchi dastur yozing
# 10.Ikkita fileda sonlar berilgan, oxshash bolmaganlarini yangi filaga yozing



from faker import Faker
fake = Faker(['uz_UZ'])
import random

# with open('test1.txt', 'w') as file:
#     for _ in range(1, 11):
#         yosh = random.randint(15, 55)
#         f = file.write(f'{fake.name()} {yosh}\n')


# # 2. test1.txt dan o'qib, yosh bo'yicha sortlash va test2.txt ga yozish
# with open("test1.txt", "r") as f:
#     lines = f.readlines()
#
#
# # Har bir qatordagi yoshni ajratib olish va sortlash
# sorted_lines = sorted(lines, key=lambda line: int(line.strip().split()[-1]))
# # print(sorted_lines)
#
#
# with open("test2.txt", "w") as f:
#     f.writelines(sorted_lines)




with open("test1.txt", "r") as f:
    lines = f.readlines()
    print(sorted(lines))



