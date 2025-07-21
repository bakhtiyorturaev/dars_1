import csv

# CSV nima?
# CSV (Comma-Separated Values) — bu oddiy matn fayli bo‘lib, unda ma’lumotlar vergul yoki
# boshqa belgi (delimiter) bilan ajratilgan bo‘ladi. Har bir qator — bu bir satrli yozuv.
#
#  CSV fayl tuzilishi:

# id,name,age
# 1,Bakhtiyor,22
# 2,Ali,25
#  CSV fayllarning afzalliklari:
#  Oddiy tuzilma
#
#  Ko‘p dasturlarda ochiladi (Excel, Google Sheets, Python, va h.k.)
#  Engil va tez ishlaydi
#  CSV fayllarning kamchiliklari:
#  Murakkab ma'lumotlar uchun mos emas (nested JSON, massivlar)
#  Har doim aniq formatlashni talab qiladi
#  Kutubxonalar:

# import csv
# import pandas as pd
#  3. CSV yozish (Python csv moduli bilan)

# import csv
# malumot = [
#     ['id', 'name', 'age'],
#     [1, 'Bakhtiyor', 22],
#     [2, 'Ali', 25],
# ]
#
# with open('students.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(malumot)


# with open('students.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# with open('students.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow([3, 'Muhammad', 23])

# import pandas as pd
#
# df = pd.read_csv('students.csv')
# print(df)
#  7. Pandas bilan CSV yozish

# df = pd.DataFrame({
#     'id': [1, 2, 3],
#     'name': ['Bakhtiyor', 'Ali', 'Muhammad'],
#     'age': [22, 25, 23]
# })
#
# df.to_csv('students_pandas.csv', index=False)
#  8. Foydali Pandas funksiyalari:




# CSV fayl yaratish: Talabalar ro‘yxati

# import csv
#
# students = [
#     ['ID', 'Name', 'Age', 'Grade'],
#     [1, 'Bakhtiyor', 22, 87],
#     [2, 'Ali', 21, 90],
#     [3, 'Malika', 23, 95],
#     [4, 'Diyor', 20, 78]
# ]
#
# with open('students.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(students)
#  2. CSV o‘qish va har bir foydalanuvchini chiroyli chiqarish

# with open('students.csv', mode='r') as file:
#     reader = csv.reader(file)
#     next(reader)
#     for row in reader:
#         print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}")

# new_student = [5, 'Ziyoda', 24, 88]
#
# with open('students.csv', mode='a', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(new_student)
# ✅ 4. CSV faylni Pandas orqali o‘qish va filtering

import pandas as pd

df = pd.read_csv('students.csv')
# print(df[df['ball'] < 70])

# avg = df['ball'].mean()
# print(f"O‘rtacha ball: {avg}")
#
# top_student = df[df['ball'] == df['ball'].max()]
# print(" Eng yuqori baho olgan:")
# print(top_student)
 # 7. Talabalar yoshiga qarab tartiblab CSV yozish



# df[['Name', 'Grade']].to_csv('students_name_grade.csv', index=False)

data = [
    {'id': 1, 'name': 'Bakhtiyor','guruhi':'Itk 2302', 'yili': 22},
    {'id': 2, 'name': 'Ali', 'guruhi': 'Itk 2201','yili': 21}
]

# with open('students_dict.csv', 'w', newline='') as file:
#     fieldnames = ['id', 'name', 'age',]
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(data)
file = 'talabalar.csv'
with open(file, 'w', newline='') as f:
    ustunlar = ['id', 'name', 'guruhi', 'yili']
    w = csv.DictWriter(f, fieldnames=ustunlar)
    w.writeheader()
    w.writerows(data)



# name = input("Ismingizni kiriting: ")
# age = input("Yoshingizni kiriting: ")
#
# with open('user_input.csv', mode='a', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow([name, age])
#     print("✅ Ma’lumot saqlandi.")



# importing the csv module
# import csv
# fields = ['Name', 'Branch', 'Year', 'GPA']
# rows = [['Nikhil', 'COE', '2', '9.0'],
#         ['Sanchit', 'COE', '2', '9.1'],
#         ['Aditya', 'IT', '2', '9.3'],
#         ['Sagar', 'SE', '1', '9.5'],
#         ['Prateek', 'MCE', '3', '7.8'],
#         ['Sahil', 'EP', '2', '9.1']]
#
# filename = "university_records.csv"
#
# with open(filename, 'w') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(fields)
#     csvwriter.writerows(rows)


# print(csvwriter.head())        # Birinchi 5 qatordan iborat qismini ko‘rsatadi
# print(csvwriter.info())        # DataFrame haqida umumiy ma'lumot
# print(df.describe())    # Statistik ma'lumot

# 1.CSV fayiliga (list, dict) malumotlarini yozish
# 2.CSV faylidan ma'lumotlarni o'qish
# 3.Binary fayliga ma'lumot yozish(fayl turi  fayl.bin)
# 4.Binary faylidan ma'lumotlarni o'qish
# 5.OS modulidan foydalanib fayl yoki papkalarni(o'chirish, o'zgartirish, yaratish)
