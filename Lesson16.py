# # Регулярные выражения 2:
# import re
# st = 'but bot bit bite bottle,rabbit bat batman'
# print(re.findall(r"b.t", st))
# print(re.findall(r"b\w*t", st))
# print(re.findall(r"...", st))
# print(re.findall(r"..t", st))
# print(re.findall(r"\bb\b", st))
# print(re.findall(r"b.*", st))
# print(re.findall(r"\b\w*b[aioeu]t\w* \w*\b", st))
# print(re.findall(r"\w*b[aioeu]t\w* \w*", st))
# print(re.findall(r"\w*b[aioeu]t\w* \w* \w*", st))
# print(re.findall(r"\w*b[aioeu]t\w* \w* \w*", st))
# print(re.findall(r"\w*b[aioeu]t\w* \w* \w* \w*", st))



# # ДЗ 15-1:
# import re
# dct = {1: 1, 2: 2, 3: {2: 22, 3: {1: 111, 2: 222, 3: {0: 1111, 1: 2222, 2: 3333}}, 1: 11, }, 6: 22}
# def dct_val(dct, x):
#     r = []
#     for k, v in dct.items():
#         if k == x:
#             r.append(v)
#         if type(v) == dict:
#             s = dct_val(v, x)
#             r.extend(s)
#     return r
# print(*dct_val(dct, 1), sep ='\n')


# \d - любая цифра
# \D - любая НЕ цифра
# Регулярные выражения в Python от просто к сложному. Подробности... Статья в Хабре
# re.sub() - замена


# import re
# text = 'fizz.123.buzz.456.fizzbuzz'
# res1 = re.sub(r'\d+', r'>>>>', text)
# res2 = re.sub(r'[a-z]+', r'(*)', text)
# print(res1)
# print(res2)


# import re
# def fullname(x):
#     s = x.group()
#     if s == 'Коля': return 'Николай'
#     elif s == 'Миша': return 'Михаил'
#     elif s == 'Таня': return 'Татьяна'
#     return s
# text = 'Коля Миша Таня Петя'
# res = re.sub(r'\b\w{4}\b', fullname, text)
# print(res)

# The same as:

# import re
# def fullname(x):
#     s = x.group()
#     match s:
#         case 'Коля': return "Николай"
#         case 'Миша': return "Михаил"
#         case 'Таня': return "Татьяна"
#         case _: return s
# text = 'Коля Миша Таня Петя'
# res = re.sub(r'\b\w{4}\b', fullname, text)
# print(res)



# import re
# def fullname(x):
#     s = x.group()
#     dct = {'LED':'Пулково', 'SVO':'Шереметьево', 'MSQ': 'Минск', 'SVX':'Кольцово'}
#     return dct.get(s, 'Unknown')
# text = 'LED ppp SVO 312321 MSQ kgjeworgn SVX'
# import re
# res = re.sub(r'\b\w{3}\b', fullname, text)
# print(res)


# import re
# def fullname(x):
#     s = x.group()
#     dct = {'LED':'Пулково', 'SVO':'Шереметьево', 'MSQ': 'Минск', 'SVX':'Кольцово'}
#     return dct.get(s, 'Unknown')
# text = 'LED ppp SVO 312321 MSQ kgjeworgn SVX'
# import re
# res = re.sub(r'LED', r'Пулково', text)
# res = re.sub(r'SVO', r'Шереметьево', text)
# print(res)


# import re
# text = 'Комольцев Сергей'
# res = re.sub(r'(Комольцев) (\w*) (Сергей)', r'\2 \1', text)
# print(res)


# import re
# text = '123 first 234 second'
# res = re.findall(r'(\d+) \w+', text)
# res = re.findall(r'(\d+) (\w+)', text)
# # res = re.findall(r'(\d+)[:, ](\w+)', text)
# print(res)


# import re
# text = 'www.itmo.ru www.yandex.ru www.CNN.com'
# res = re.findall(r'www.(\w+).(?:ru|com)', text)
# print(res)


# import re
# text = 'abracadabra'
# res = re.findall(r'a', text)
# print(res)


# # Finditer
# import re
# text = 'abracadabra'
# res = re.finditer(r'abr', text)
# for i in res:
#     print(i.group(), i.start(), i.end())


# # Код должен корректно считать количество замен и заменять все `a` на `A` с порядковыми номерами:
# import re
# def fu(text):
#     counter = 0
#     def change(x):
#         nonlocal counter
#         counter += 1
#         return 'A' + str(counter)
#     res = re.sub('a', change, text)
#     return res
# print(fu('aaaaaaaaaaaaaaaaaa'))


# # Эта функция ищет все совпадения с шаблоном "a" в строке "text" и выводит номер совпадения,
# # само совпадение, а также индексы начала и конца этого совпадения в строке.
# import re
# text = 'abracadabra'
# res = re.finditer(r'a', text)
# for j, i in enumerate(res):
#     print(j, i.group(), i.start(), i.end())


# import re
# def fu(text):
#     counter = 0
#     def change (x):
#         nonlocal counter
#         counter += 1
#         return 'A'+str(counter)
#     return re.sub(r'a', change, text)
# print(fu('abracadabra'))




# # Буква повторяется два и более раз
# import re
# text = 'Гамма Адажио Аллегро Нота До Ре Фортиссимо'
# res = re.findall(r'\b\w+\b', text)
# import collections
# for i in res:
#     x = collections.Counter(i).values()
#     if max(x) > 1:
#         print(i, max(x))



# import re
# text = '1         + 2222 * 3  -  7'
# print(re.split(r'\s+', text))