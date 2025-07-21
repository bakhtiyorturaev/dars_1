
mevalar = ['olma', 'anor', 'uzum', 'nok', 'behi', 'olma', 'uzum']
sonlar = [3, 455, 6, 5, 2, 546, 564, 45, 34]
aralash = [54, 56, 'spark', 'malibu', True, False]

# a = len(mevalar)
# b = len(sonlar)
# print(a)
# print(b)

# new_list = list(('malibu', 'cobalt'))
# print(new_list)

# indexlar

# mevalar[2] = 'qulupnay'
# print(mevalar)

# a = mevalar[::-3]
# b = sonlar[::-3]

# print(a)
# print(b)

# a = mevalar[0:2] = ["1", "2"]
# print(mevalar)
# print(a)

# mevalar.append('12345366')
# print(mevalar)

# mevalar.insert(0, 'uzum')
# print(mevalar)

# mevalar.extend(sonlar)
# print(mevalar)

# mevalar.remove('uzum')
# print(mevalar)

# sonlar.pop()
# print(sonlar)

# del sonlar[-1]
# print(sonlar)

# sonlar.clear()
# print(sonlar)

# sonlar.sort(reverse=True)
# mevalar.sort(reverse=True)
#
# print(sonlar)
# print(mevalar)


# sonlar.reverse()
# print(sonlar)

# a = sonlar.copy()
# print(a, sonlar)

# a = sonlar.count(2)
# b = mevalar.count('olma')
# print(a)

# a = sonlar.index(2)
# print(a)


mevalar = ['olma', 'anor', 'uzum', 'nok', 'behi', 'olma', 'uzum']
#
# for meva in mevalar:
#     for harf in meva:
#         print(harf)


a = [i for i in sonlar if i != 0 ]
print(a)