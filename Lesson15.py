# a = [i for i in range(10)]
# b = (i for i in range(10))
# c = {i for i in range(10)}
# d = {x: x**2 for x in range(10)}
# print(a)
# print(b)
# print(c)
# print(d)


# # Перевернутая пирамида:
# def fun(n, d=0):
#     if n == 1:
#         print(' ' * d + '* ' * n)
#         return
#     else:
#         print(' ' * d + '* ' * n)
#         fun(n - 1, d + 1)
#         # print(' ' * d + '* ' * n)
# fun(int(input('Введите число: ')))


# # finally выполняется всегда:
# def f(x,y):
#     try:
#         return x / y
#         print(123)
#     except:
#         return x, y
#         print(456)
#     finally:
#         print('finally')
# print(f(1,2))


# # * Рекурсия, факториал:
# f = 1
# for i in range(2, int(input())):
#     f *= i
# print(f)


# # Фибаначи, меньше какого-то введенного значения:
# res = {1: 0, 2: 1}


# def fibo(n):
#     if n not in res:
#         if n == 1:
#             return 0
#         elif n == 2:
#             return 1
#         else:
#             res[n] = fibo(n-1) + fibo(n-2)
#     return res[n]
# print(fibo(20))
# print(res)


# # Появился с 3.10!
# def feb(n):
#     match n:
#         case 1: return 0
#         case 2: return 1
#         case 3: return fibo(n-1) + fibo(n-2)
# print(fibo(20))


# import sys
# print(sys.version)


# lst = [1, 'a', 2, [11, 'cd', 22, [111, 222, [1111, 'sd', 2222, 3333], 333, 444, [555, 666]], 3], 4]
# def numb(lst):
#     res = []
#     for i in lst:
#         if type(i) == int:
#             res.append(i)
#             print('--->', res)
#         elif type(i) == list:
#             res.extended(numb(i))
#             print('===>', res)
#     return res
# print(numb(list))


# def numb(lst):
#     res = []
#     for i in lst:
#         if type(i) == int:
#             res.append(i)
#             print('---', res)
#         elif type(i) == list:
#             res.extend(numb(i))
#             print('===', res)
#     return res


# print(numb(lst))


# import re
# print('ab3548b45v'.find('8'))

# import re
# # re.findall()
# string = 'Числа 99, 72, 81 и 999 делятся на 9'
# print(re.findall(r"\d{2}", string))
# print(re.findall(r"\d, \d", string))
# #  Точка . все

# string = 'Чис ла 99, 72, 81 и 999 дел, ятся'
# re.findall(r'[+-]?\d+', string)


# import re
# s = '0abracadabra1'
# regex = r'.a.'
# # r - любой символ, точка - тоже любой символ, т.е. нам нужен любой где в середине "а"
# regex1 = r'\da\w'
# print(re.findall(regex, s))
# print(re.findall(regex1, s))


# import re
# s = '1 123 324 345 66 2 1 1123'
# regex = r'\b1\d\d\b'
# print(re.findall(regex, s))


# import re
# s = 'Косой покосой косил траву на косе'
# regex = r'\b\w+\b'
# regex1 = r'\b[Кк]ос\w+\b'
# regex2 = r'\b\w*кос\w*\b|\b\w*Кос\w*\b'
# print(re.findall(regex, s))
# print(re.findall(regex1, s))
# print(re.findall(regex2, s))


# import re
# s = 'Косой покосой косил траву на косе'
# regex = r'\b\w*кос\w*\b'
# print(re.findall(regex, s))


# s = 'cat cet cit cot cut c#t c{t c2t'
# import re
# # regex = r'c.t'
# # regex = r'[aeu]t'
# # regex = r'c[a-i]t'
# regex = r'c[^a-i]t' # Ни одного из этих символов
# print(re.findall(regex, s))


# \d - любая цифра
# \D - любой нецифровой символ
# \w - любой алфовитно-цифровой символ
# \W - любой НЕ алфовитно-цифровой символ
# \s - любой пробельный символ
# \s - любой НЕ пробельный символ
# \d{1,3} - от 1 до 3
# \w{2} - ровно две буквы
# \d{2,} - две и больше цифры
# \w{,3} - не больше 3 символов


# s = 'A123BC78 X987YZ178 P777PP178 V666VV147'
# import re
# regex = r'[A-Z]\d\d\d[A-Z]{2}1?78'
# print(re.findall(regex, s))


import re
s = 'Java blablabla Javascript'
res, n = re.subn(r'Java\w*', r'Python', s)
print(res, n)
# n - сколько раз произошла замена


# В регулярных выражениях символ "+" обозначает, что предшествующий шаблон должен повторяться один
# или несколько раз. В данном контексте, если в строке найдется слово, начинающееся с "Java" и за
# которым идет один или несколько символов слова (буквы, цифры или символы подчеркивания), оно будет
# заменено на "Python".

# Символ "*" в регулярных выражениях обозначает, что предшествующий шаблон может повторяться ноль или
# несколько раз. В данном контексте, если в строке найдется слово, начинающееся с "Java" и за которым
# могут идти ноль или более символов слова (буквы, цифры или символы подчеркивания), оно будет заменено
# на "Python".


# # Четные числа
# s = '0 1 2 3 12 22 5 42 43 35 17 100'
# import re
# res = re.findall(r'\d*[02468]', s)
# print(res)


# # Кратные пяти числа
# s = '0 1 2 3 12 22 5 42 43 35 17 100'
# res = re.findall(r'\b\d*[05]\b', s)
# print(res)
