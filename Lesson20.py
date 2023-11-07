# Numpy (нампАй), pandas сегодня


# a = {True: '1', 1:'one'}
# print(a)
# n = {1: 'a', True:'one'}
# print(n)
# b = {False: '0', 0: 'Zero'}
# print(b)
# c = {0: '0', False: 'Zero'}
# print(c)


# # Магические методы сравнения:
# __eq__ - определяет поведение оператора равенства
# __ne__ - ... неравенства
# it - меньше
# gt - больше
# le, ge - меньше или равно и больше или равно


# class A:
#     def __init__(self, limit):
#         self.limit = limit
#         print(self.limit)
#     def __next__(self):
#         self.limit -= 1
#         print(self.limit)
#         if self.limit <= 0:
#             raise StopIteration
#         else:
#             return 1111
#     def __iter__(self):
#         return self
# b = A(10)
# for i in b:
#     print(next(b))


# import itertools
# # print(dir(itertools))
# for x in itertools.permutations([1,2,3,4]):
#     print(x, end = '')
# print(' ')
# for x in itertools.combinations_with_replacement([1,2,3,4], 3):
#     print(x, end = '')
# print(' ')
# x = itertools.cycle([1,2,3,4])
# for i in range(10):
#     print(next(x))


# import itertools
# for x in itertools.chain([0,1,2], 'abcde'):
#     print(x)


# x = 0
# for _ in range (10):
#     x = 1 - x
#     print(x)


# import itertools
# for x in itertools.zip_longest([1,2,3], 'abcde', fillvalue = 0):
#     print(x)


# # Группирует по буквам
# import itertools
# s = 'aaaaabbbbcccc'
# for k, v in itertools.groupby(s):
#     print(k, ':', *v)


# import itertools
# s = 'aaaa123abb321bbccc231c'
# for k, v in itertools.groupby(s, key = lambda x:x.isdigit()):
#     print(k, ':', *v)


# import itertools
# def odd(x):
#     return bool(x%2)
# s = [1,2,3,4,5,15,25,36,47,57,88,100,6]
# for k, v in itertools.groupby(s, key = odd):
#     print(k, ':', *v)


# import itertools
# def pos_neg(x):
#     return x > 0
# s = [-1, -2, -3, 1, 2, 0, 3, 4, -10, -7, -2]
# for k, v in itertools.groupby(s, key=pos_neg):
#     print(k, ":", *v)


# numpy - библиотека Python для математических вычислений


import numpy as np
# arr = np.array([5,2,3,4,5,6,7,'0'])
# # print(type(arr))
# # print(arr)
# for i in arr:
#     print(i)
# print(sorted(arr))
# print(max(arr))
# print(arr.shape)


# arr1 = np.zeros(10, dtype = int)
# arr2 = np.zeros((2, 3), dtype = int)
# print(arr1)
# print(arr2)


# # Должно работать но я не разобрался:
# brr = arr2.reshape((2,2))
# print(brr)


# a1 = np.array([[1,2,3], [10,20,30]])
# print(a1)
# print(np.sum(a1))
# print(np.sum(a1, axis = 0))
# # Суммируем элементы в столбике. По X & Y


# a2 = np.array([[27, 2.1, 3.7],[24,12,75]])
# print(np.cbrt(a2))
# print(np.gcd([17,25,80],[24,12,36]))
# # gcd - наибольший общий делитель (поэлементно)
# # lcm - наименьшее общее кратное


# Визуализация данных (графики). Пандас на этом работает
import numpy as np
import matplotlib.pyplot as plt


# x = np.linspace(-2, 5, num=50)
# y = np.exp(x)
# plt.plot(x, y)
# plt.grid()
# _ = plt.title('exp')
# plt.show()


# # nan - нет данных
# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
# print(np.mean(x))
# print(np.average(x))
# print(np.nanmedian(x))
# print(np.median(x))
# print(np.max(x))
# print(np.percentile(x, 50))
# x2 = np.array([1, 2, 3, 4, 5, 6, 7, 0, 9, 0])

# # Поэлиментно
# print(x == x2)
# print(x > x2)


# arr = np.array([2, 3, 4, 5, 6, 8, 11, 123])
# cond = arr < np.percentile(arr, 25)
# print(arr[cond])


# y1 = np.array([1, 2, 4, 6, 7, 8, 2, 33, 23, 55, 34])
# y = x*2
# print(x)
# print(y)
# np.where(x > 5, x, y)
# y2 = np.array([[3, 5, 1, 8, 18], [17, 3, 10, 15, 14]])
# sa = np.sort(y2, axis=1)
# print(sa)


# # Разбивает от 0 до введенного числа и кладет в массивчики
# import numpy as np
# n = int(input('Imput: '))
# res, init = [], 0
# for i in range(n):
#     cur = []
#     for j in range(n):
#         init += 1
#         cur.append(init)
#     res.append(cur)
# print(res)
# # Как квадратная матрица:
# arr = np.array(res)
# print(arr)
# print(np.median(arr, axis = 0))
# print(np.median(arr, axis = 1))


# pandas = panel data - похож на Эксель
# есть pd.Series и pd.DataFrame (Мы делаем акцент на втором)
# import pandas
import pandas as pd
# Делает красиво как в экселе
# df1 = pd.DataFrame([[1, 'Bob', 'Builder'],
#                    [2, 'Sally', 'Baker'],
#                    [3, 'Scott', 'Master']])
# df1.columns = ['id', 'name', 'pro']
# print(df1[['name', 'pro']])
# # Из-за двух квадратных скобок не работало
# print(df1)


# df2 = pd.DataFrame({
#     'country': ['KZ', 'RU', 'BY', 'UA'],
#     'popul': [12,234,345,456],
#     'sq': [111,222,333,444]
# })
# print(df2)

# # Заглавная или строчная буква разница есть!

# df = pd.DataFrame({'Id':['F','S','T'], 'FIO':['ABC','XYZ','SRT']})
# df['Salary'] = [213,234,345]
# df['Plus'] = df['Id'] + df['FIO']
# df['Nalog'] = (df['Salary'])*0.13
# print(df)


dct = {'Год:': [2001, 2002, 2003, 2004, 2005],
       'Товар:': ['A', 'B', 'C', 'D', 'E'],
       'Шт:': [10, 20, 30, 35, 3],
       'Цена:': [60, 50, 8, 25, 40]}

df = pd.DataFrame(dct)
df['Итог:'] = df['Шт:'] * df['Цена:']
df.index = df['Год:']
print(df)
df['Итог:'].plot(kind='barh')
plt.show()


df1 = pd.DataFrame()
df1.index = df['Год:']
df1['Итог:'] = df['Итог:']
print(df)
df.to_excel('dct.xlsx')
df1 = pd.read_excel('dct.xlsx')
print(df1)
