#
#
# def ReactPS(x1, y1, x2, y2):
#     yuzi_x = x1 * x2
#     yuzi_y = y1 * y2
#     peremetr_x = 2 * (x1 + x2)
#     peremetr_y = 2 * (y1 + y2)
#
#     print("yuzi x:",yuzi_x, "yuzi y:", yuzi_y, "peremetri x: ",peremetr_x, "peremetri y: ",peremetr_y)
#     return yuzi_x
#
# x1 = int(input("x1 ni kiriting: "))
# y1 = int(input("y1 ni kiriting: "))
# x2 = int(input("x2 ni kiriting: "))
# y2 = int(input("y2 ni kiriting: "))
#
# print(ReactPS(x1, y1, x2, y2))
#
#
#
# # - return
# # - *args, **kwargs
# # rekursiv funksiya
#
#
#
# def faktorial(n):
#     if n == 1:
#         return n
#     return n * faktorial(n-1)
#
# # n = int(input("n: "))
# #
# # a = faktorial(n)
# # print(a)
#
# def faktorial(n):
#     if n == 1:
#         return n
#     a = 1
#     for i in range(1, n+1):
#         a *= i
#     return a
#
# n = 5
#
# b = faktorial(n)
# print(b)

from dars_6 import SordLnc

a, b, c = map(int, input().split())

d = SordLnc(a, b, c)

print(d)