# # match case
# a = int(input("a-son: "))
# b = int(input("b-son: "))
# c = int(input("c-son: "))
#
# if a > b and a > c:
#     print("a soni eng kattasi")
#     if b > c:
#         print("b o'rtachasi")
#     else:
#         print("c eng kichigi")
#
# elif b > a and b > c:
#     print(" b eng katta son")
#     if a > c:
#         print("a o'rtachasi")
#     else:
#         print("c eng kichigi")
#
# elif c > a and c > b:
#     print(" c eng katta son")
#     if a > b:
#         print("a o'rtachasi")
#     else:
#         print("b eng kichigi")







# operator = input(" operatorlarnidan birini kiriting: (+, -, *, / --> )")
#
# x = 5
# y = 10
#
# match operator:
#     case '+':
#         natija = x + y
#     case '-':
#         natija = x - y
#     case '*':
#         natija = x * y
#     case '/':
#         natija = x / y
#
# print(natija)


kun = int(input(" kunni kiriting: "))

match kun:
    case 1:
        print("Dushanba")
    case 2:
        print("Seshanba")
    case 3:
        print("Chorshanba")
    case 4:
        print("Payshanba")
    case 5:
        print("Juma")
    case 6:
        print("Shanba")
    case 7:
        print("Yakshanba")
    case _:
        print("Bunday kun mavjud emas")




kun = 5

match kun:
    case 6 | 7:
        print("Bugun dam olish kuni")

    case 1 | 2 | 3 | 4 | 5:
        print("Bugun ish kuni")

    case _:
        print("bunday kun mavjud emas!")










a,b,c = map(int, input("sonlarni kiriting:").split())
print(a)
print(b)
print(c)












