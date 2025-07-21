#
#
# def salom(ism):
#     """
#     bu Salom beruvchi funksiya
#     """
#     print(f"{ism} salom xush kelibsiz")
#

# salom("Baxtiyor")
#
#
# def kvarat(a, b=2):
#     k = a ** b
#     print(k)
#
# a = int(input("a: "))
# b = int(input("b: "))
# kvarat(b, a)
#
#
#
#
# # def talaba(ism, familiya, tugilgan_yil):
# #     yosh = 2025 - tugilgan_yil
# #
# #     print(f"Salom {ism} {familiya} sizning yoshingiz {yosh}")
# #
# #
# #
# # talaba("Baxtiyor", "Turayev", 2001)
#
#
#
# def myfunc():
#   global x
#   x = "fantastic"
#
# myfunc()
#
# print("Python is " + x)
#
#
#
#
#
#
#
#
#
# # - def(),
# # - funksiya kvartarga oshirish
# # - default qiymat
# # - funksiya o’quvchilar ma’lumotlari funksiyasi.
# # - global va locak o’zgaruvchilar
# #
# # talaba_info("Baxtiyor", 21)                # Positional
# # talaba_info(yosh=21, ism="Baxtiyor")       # Keyword
# # - return
# # - *args, **kwargs





# def PowerA3(A, B, C, D, E):
#     print(f"{A} ning 3 darajasi {A ** 3}")
#     print(f"{B} ning 3 darajasi {B ** 3}")
#     print(f"{C} ning 3 darajasi {C ** 3}")
#     print(f"{D} ning 3 darajasi {D ** 3}")
#     print(f"{E} ning 3 darajasi {E ** 3}")
#
#
# a, b, c = map(float, input("a, b va c sonini kiriting").split())
# d, e = map(int, input("d va e sonini kiriting").split())
#
# PowerA3(a,b,c,d,e)




#11-masala

def MinMax(X, Y):
    if X < Y:
        return f'{X} kichik, {Y} katta'
    elif Y < X:
        Y, X = X, Y
        return f'{Y} katta, {X} kichik'
    else:
        return 'ikkalasa son teng'


# print(MinMax(34, 8))
a = 2
b = 5
c = 1
d = 9

a1 = MinMax(b, a)
a2 = MinMax(c, d)
a3 = MinMax(a1, a2)

# print(max(a4), min(a4))

# print(a1)
# print(a2)
# print(a3)


# def MinMax(x, y):
#     if x > y:
#         x, y = y, x
#     return x, y
#
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# d = int(input("d = "))
#
# a, b = MinMax(a, b)
# c, d = MinMax(c, d)
# a, c = MinMax(a, c)
# b, d = MinMax(b, d)
#
# print("Eng kichik son:", a)
# print("Eng katta son:", d)


def SordLnc(a, b, c):
    if (a > b and a > c) and (a > b > c):
        return a, b, c

    elif (b > a and b > c) and (b > a > c):
        return b, a, c

    elif (c > a and c > b) and (c > b > a):
        return c, b, a

    elif (c > a and c > b) and (c > a > b):
        return c, a, b

    elif (a > c and a > b) and (a > c > b):
        return a, c, b

    else:
        return 'barcha sonlar teng'


print(SordLnc(3,3,4))


