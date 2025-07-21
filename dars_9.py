# avtomobil = ('cobalt', 'matiz', 'spark', 'malibu', 2, 5, True, 2, 'malibu')

# print(len(avtomobil))

# print(avtomobil[3:])
# print(avtomobil[6])

# del avtomobil
# print(avtomobil)

# for i in avtomobil:
#     print(i)

# print(avtomobil.count(2))

# list_avtomobil = list(avtomobil)
# print(list_avtomobil)



#SET

# avtomobil = {'cobalt', 'matiz', 'spark', 'malibu', 2, 5, True, 2, 'malibu'}
# elektromobil = {'tesla', 'BWD', 'BMW', 'MERC', 'malibu', True, 5}


# print(avtomobil)
# print(len(avtomobil))

# avtomobil.add('onix')
# print(avtomobil)
# print(elektromobil)


# avtomobil.update(elektromobil)
# print(avtomobil)


# avtomobil.remove('matiz')
# avtomobil.discard('aaaaaa')
# print(avtomobil)

# print(elektromobil)
# elektromobil.pop()
# print(elektromobil)


# avtomobil.clear()
# print(avtomobil)

# a = avtomobil.union(elektromobil)
# print(avtomobil)
# print(a)

# b = avtomobil.intersection(elektromobil)
# print(b)
#
# avtomobil.symmetric_difference_update(elektromobil)
# print(avtomobil)
#
# c = avtomobil.symmetric_difference(elektromobil)
# print(c)




# def uchta_son(son1, son2, son3):
#     if son1 % 2 == 0 or son2 % 2 == 0 or son3 % 2 == 0:
#         print(True)
#     else:
#         print(False)
#
# son1 = 7
# son2 = 10
# son3 = 5
# print(uchta_son(son1, son2, son3))



# def uchta_son(son1, son2, son3):
#     if (
#             (son1 % 2 != 0 and son2 % 2 == 0)
#             or (son3 % 2 != 0 and son2 % 2 != 0)
#             or (son3 % 2 != 0 and son1 % 2 != 0)
#     ):
#         print(True)
#     else:
#         print(False)
#
# a = 3
# b = 3
# c = 11
#
# print(uchta_son(a, b, c))

