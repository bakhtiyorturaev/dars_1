
# my_info = {
#     'ism': 'Baxtiyor',
#     'familiya': 'Turayev',
#     'yosh': 24,
#     'kasbi': 'dev'
# }

# print(len(my_info))


# print(my_info['yosh'])

# print(my_info.get('job'))

# print(my_info.keys())
# print(my_info.values())

# print(my_info.items())

# my_info['name'] = 'Baxti'
# print(my_info)

# my_info.update({'name': 'Baxti2'})
# print(my_info)


# my_info.pop('yosh')
# print(my_info)

# my_info.popitem()
# print(my_info)

# del my_info['familiya']
# print(my_info)

# del my_info
# print(my_info)

# my_info2 = my_info.copy()

# print(my_info)
# print(my_info2)

# my_info3 = dict(my_info)
# print(my_info3)


# for i in my_info2.values():
#     print(i)

# for i, j in my_info2.items():
#     print(i, j)



# D = {
#     'key1': {'name': 'Baxtiyor', 'ishi': 'dasturchi'},
#     'key2': {'name': 'Ali', 'ishi': 'backend dev'},
#     'key3': {'name': 'Vali', 'ishi': 'frontend dev'}

# }

# print(D['key1'])
#
# for i in D.values():
#     print(i['ishi'], i['name'])


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#
# # x = car.setdefault("model", "Bronco")
# y = car.setdefault("year", 2000)
# x = car.setdefault("color", "white")
#
#
# print(x)
# print(y)





# def lotin_to_kiril(text):
#     harflar = {
#         'yo': 'ё', 'gʻ': 'ғ', 'oʻ': 'ў', 'sh': 'ш', 'ch': 'ч', 'yu': 'ю', 'ya': 'я',
#         'a': 'а', 'b': 'б', 'd': 'д', 'e': 'е', 'f': 'ф', 'g': 'г', 'h': 'ҳ',
#         'i': 'и', 'j': 'ж', 'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о',
#         'p': 'п', 'q': 'қ', 'r': 'р', 's': 'с', 't': 'т', 'u': 'у', 'v': 'в',
#         'x': 'х', 'y': 'й', 'z': 'з'
#     }
#
#     i = 0
#     result = ""
#     text = text.lower()
#
#     while i < len(text):
#         if i + 2 <= len(text) and text[i:i+2] in harflar:
#             result += harflar[text[i:i+2]]
#             i += 2
#         else:
#             result += harflar.get(text[i], text[i])
#             i += 1
#
#     return result
#
# print(lotin_to_kiril("chyot"))



# def kiril_to_lotin(matn):
#     harflar = {
#         'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
#         'ж': 'j', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
#         'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
#         'ф': 'f', 'х': 'x', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sh', 'ъ': '',
#         'ы': 'i', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya', 'ғ': 'gʻ', 'қ': 'q',
#         'ҳ': 'h', 'ў': 'oʻ'
#     }
#     return ''.join(harflar.get(c, c) for c in matn.lower())
#
# print(kiril_to_lotin("ассалом"))








def lotin_to_kril(text):
        harflar = {
                'yo': 'ё', 'gʻ': 'ғ', 'oʻ': 'ў', 'sh': 'ш', 'ch': 'ч', 'yu': 'ю', 'ya': 'я',
                'a': 'а', 'b': 'б', 'd': 'д', 'e': 'е', 'f': 'ф', 'g': 'г', 'h': 'ҳ',
                'i': 'и', 'j': 'ж', 'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о',
                'p': 'п', 'q': 'қ', 'r': 'р', 's': 'с', 't': 'т', 'u': 'у', 'v': 'в',
                'x': 'х', 'y': 'й', 'z': 'з'
            }
        i = 0
        result = ""
        text = text.lower()

        while i < len(text):
                if i + 2 <= len(text) and text[i:i+2] in harflar:
                    result += harflar[text[i:i+2]]
                    print(result)
                    i += 2

                else:
                    result += harflar.get(text[i], text[i])
                    i += 1

        return result



print(lotin_to_kril('salom'))

# print('shamol'[0:2])
























