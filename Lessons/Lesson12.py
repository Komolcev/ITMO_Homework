# a = [1,2,3,4]
# b = a
# a = a + [5,6,7,8]
# print(a)


# c = [1,2,3,4]
# d = c
# c += [5,6,7,8]
# print(c)
# print(d)


# # timedelta - разница времени
# import datetime, locale
# locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
# a = datetime.datetime.today() + datetime.timedelta(days = 14)
# print(a)
# c = datetime.timedelta(days=1)
# for _ in range(10):
#     a += c
#     print(a.strftime('%A %d, %B %Y'))
# # День недели, номер дня, месяц, год, можно вместо B поставить m


# import datetime, locale
# print(datetime.datetime.strptime('22/04/2023 19:33', '%d/%m/%Y %H:%M'))


# import calendar
# year, month = tuple(map(int, input('Введите год и месяц: ').split()))
# print(year, month)
# print(*calendar.monthcalendar(year, month))


# # Модуль для очень удоного перебора:
# import itertools
# for i in itertools('abc', [1,2,3,4,5]):
#     print(i)


# import itertools
# for i in itertools.chain('abcd', [1,2,3,4], (11,12,13,14)):
#     print(i, end = ' ')


# lst = [[1,2,3],[11,22,33],[111,222,333]]
# print(*lst[0])
# print(type(lst))
# for i in itertools.chain(*lst):
#     print(i, end = ' ')
# print()
# for i in itertools.chain(lst):
#     print(i, end = ' ')


# for i in zip ('abc', [11,22,33,44], (111,222,333,444,555,666)):
#     print(i)


# import itertools
# for i in itertools.zip_longest('abc', [11,22,33,44], (111,222,333,444,555), fillvalue = -1): # Можно пустую строку, None, True и т.д.
#     print(i)


# # Тернанрный оператор:
# x = 1
# y = 2
# maxi = x if x > y else y
# print(maxi)


# number = 5
# abso = number if number >= 0 else -number
# print(abso)


# def flip_flop(x):
#     print(x)
#     return 'flip' if x == 'flop' else 'flop'


# x = 'flip'
# for _ in range(5):
#     x = flip_flop(x)
#     print('--->', x)


# # List comprehesion ("включение в список" или "список включения"):
# print([x for x in range(5)])


# # то же самое что и:
# lst = []
# for x in range(5):
#     lst.append(x)
# print(lst)


# # Квадраты:
# print([x**2 for x in range(10)])


# # Четные квадраты:
# lst1 = []
# for x in range(10):
#     if x % 2 == 0:
#         lst1.append(x**2)
# print(lst1)


# # Четные квадраты 2:
# print([x**2 for x in range(10) if x % 2 == 0])


# print(list(map(lambda x: x**2, range(15))))


# print([x**2 for x in range(20) if x % 3 == 0])


# print([x for x in range(21) if x % 2 == 0])


# # Замена отрицательных числен нулями:
# lst = [1,0,-1,2,23,-18,5,0,26,-11]
# new_lst = [i   if i > 0 else None   for i in lst]
# print(new_lst)


# # Взять отрицательные, а положительные заменить на три девятки:
# lst1 = [1,0,-1,2,23,-18,5,0,26,-11]
# new_lst1 = [i   if i < 0 else 999   for i in lst1]
# print(new_lst1)


# # Условние в начале включения:
# from string import ascii_letters
# # print(ascii_letters)
# letters = 'abп23cABо2Cакб3вА6нjБВ'
# print([f'{let}-ДА!' if let in ascii_letters else f'{let}-НЕТ!' for let in letters])


# # Only vowels left:
# s = input('Введите слово: ')
# vowel = [i for i in s if i in 'aeiouAEIOU']
# добавь i если i есть в ... примени это для каждого элемента в s
# print(''.join(vowel))
# vowel1 = [i if i in 'aeiouAEIOU' else '_' for i in s]
# print(''.join(vowel1))


# def fb(x):
#     if x % 15 == 0:
#         return 'FB'
#     elif x % 3 == 0:
#         return 'F'
#     elif x % 5 == 0:
#         return 'B'
#     else:
#         return x
# x = int(input())
# for i in range(x):
#     print(fb(i), end = ' ')
# # print(fb(x))

# # as same as:
# print()

# def fb(x):
#     return "FB" if x%15 == 0 else 'F' if x%3 == 0 else 'B' if x%5 == 0 else x
# for i in range(x):
#     print(fb(i), end = ' ')


# words = ['Я', 'изучаю', 'Питон']
# res = [letters for word in words for letters in word]
# print(res)


# # Вложенная генерация
# key = ['name', 'age', 'weight']
# value = ['Lilu', '25', '100', True]
# print([{x,y} for x in key for y in value])
# print([(x,y) for x in key for y in value])


# matrix = [[i**j for i in range(5)] for j in range (5)]
# print(matrix)


# # Вытащить из матрицы числа и сделать в один список:
# matrix = [[0,1,2], [3,4,5], [6,7,8]]
# print(matrix)
# flat = [num for row in matrix for num in row]
# print(flat)


# a = [x for x in range(100)] # Сгенирировали список с 100
# # print(a)
# b = (x for x in range(100)) # Сгенирировали выражение, которое может это сделать
# # for i in b:
# #     print(i)
# # Те есть разница между списковым и генеративным выражением!
# print(type(a), type(b))

# import sys
# print(sys.getsizeof(a), sys.getsizeof(b))
# # Огромная разница в размере


# d = {}
# for key in range(1,10):
#     d[key] = key ** 2
# print(d)

# # as same as
# print()

# d = {key:key**2         for key in range(1,10)}
# print(type(d))
# print(d)


# d = {key:key**2         for key in range(1,10)       if key == 0}
# print(d)


# # Фильтрация
# ages = ['a':12,'b':45,'c':17, 'd':36]
# ff = {k:v for k,v in ages.items() if v > 16 if v % 2 == 0}
# # or
# ff = {k:v for k,v in ages.items() if v > 16 and v % 2 == 0}
# print(ff)


# names = ['Harry','Hermione','Ron','Neville','Luna']
# index = {k:v for (k, v) in enumerate(names)}
# print(index)
# {'Harry':0,'Hermione':1,'Ron':2,'Neville':3,'Luna':4}


# dig = ['ноль', 'один', 'два', 'три']
# d = {k: v for k, v in enumerate(dig)}
# def int_to_word(x): # возьми икс
#     str_x = str(x) # сделай его str и положи в str_x
#     # 0123 - наприме то, что мы ввели
#     return print(' '.join([d[int(i)] for i in str_x]))
#     # [d[int(i)] - вот это сука значит зайди в d и вытащи оттуда значение
#     # а теперь этот элемент значение (строка) найди в d в ключах и найди от него значение и верни его
# int_to_word(int(input('---> ')))


# # Функция которая принимает в качестве аргумента другую функцию
# from functools import cmp_to_key
# def ff(x, y):
#     if x > y:
#         return 1
#     elif x == y:
#         return 0
#     else:
#         return -1
# lst = [1, 5, 2, -3, 4, 0]
# a = sorted(lst, key=cmp_to_key(ff))
# print(a)

# 'i for i' - значит
