import csv
# faylga yozish
# with open('talabalar.csv', 'w', newline='') as file:
#     ustunlar = ['id', 'name', 'guruhi', 'yili']
#     writer = csv.DictWriter(file, fieldnames=ustunlar)
#     writer.writeheader()
#
#     data = [
#         {'id': 1, 'name': 'Bakhtiyor', 'guruhi': 'A', 'yili': 2000},
#         {'id': 2, 'name': 'Ali', 'guruhi': 'B', 'yili': 2001},
#         {'id': 3, 'name': 'Malika', 'guruhi': 'C', 'yili': 2002},
#         {'id': 4, 'name': 'Diyor', 'guruhi': 'D', 'yili': 2003},
#         {'id': 5, 'name': 'Ziyoda', 'guruhi': 'E', 'yili': 2004},
#         ]
#
#     writer.writerows(data)


# fayldan o'qish
# with open('talabalar.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     for i in reader:
#         for k in i.values():
#             print(k)
        # print(row)


# arr = [1,2,3,4,5,6,7,8,9,10, 'salom', 'python', True, False]

# with open('sonlar.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(arr)







# try:
#     print(2/a)
# except NameError:
#     print('Bunaqa ozgaruvbchi yoq')
# except ZeroDivisionError:
#     print("0 ga bo'linmaydi")



# mkdir() - yangi papka yaratadi;
# rmdir() - papkani o'chiradi;
# rename() - fayl nomini oʻzgartiradi;
# remove() faylni o'chiradi.
import os
#Skirpt joylashgan adresga nisbiy yo'l
# os.mkdir("dars4")
# absolyut adres
#os.mkdir("c://somedir")
#os.mkdir("c://somedir/hello")
#os.rename("C://Some Dir/somefile.txt",
# "C://Some Dir/hello.txt")
#os.remove("C://Some Dir/hello.txt")
# filename = input ("dars4")
# a = os.path.exists(filename):
# print("ko'rsatilgan fayl mavjud")
# else:
# print("Fayl mavjud emas")

# file = os.path.exists(filename)
# print(file)


# try:
#     with open('talaba.csv', 'r') as file:
#         reader = csv.DictReader(file)
#
# except FileNotFoundError as e:
#     print(e)


# try:
#     print(2/0)
#
# except ZeroDivisionError:
#     print("0 ga bo'linmaydi")
#
# else:
#     print("try ishladi")
#
#
# finally:
#     print("finally ishladi")


# try:
#     a = 1999
#     if a < 2999:
#
#         raise ValueError("please add money")
#     else:
#         print("Eligible")
#
# except ValueError as e:
#     print(e)

# arr = ['salom', 'python', True, False]
# try:
#     print(arr[4])
# except IndexError:
#     print("Bunday index yoq")



# arr = ['salom', 'python', True, False]
# try:
#     print(arr[4])
# except IndexError:
#     print("Bunday index yoq")



