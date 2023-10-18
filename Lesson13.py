# total = 0
# with open('test.txt', encoding='ru_RU.UTF-8') as file:
#     for i in file.readlines():
#         total = total + 1
# print(total)


# # ДЗ (12-2):
# print(*[i for i in range (1,11) for _ in range (i)])
# print(','.join([i for i in range (1,11) for _ in range (i)]))
# # Сделай для нас список i для i в диапозоне 10и раз и повторяй это i с помощью другого цикла i раз


# s = [i for i in range (11) for j in range(i)]
# print(s)


# # ДЗ (12-3):
# t = [p.split('-') for p in input().split(',')]
# print(t)
# print([k for p in t for k in range(int(p[0]), int(p[1]) +1)])


# print(list(map(lambda x: x**3, range(10))))
# # the same as:
# print([x**3 for x in range(10)])


# a = tuple((i for i in range (5)))
# print(a)
# # Функция tuple() в данном случае создает кортеж. Внутри скобок мы передаем генераторное выражение,
# # которое генерирует числа от 0 до 4 (range(5)).


# a = [i**3 if i%2 else i**2 for i in range(1,11)]
# print(a)
# # # the same as:
# a = [i**3 if i%2 == 1 else i**2 for i in range(1,11)]
# print(a)


# import functools
# print(functools.reduce(lambda x,y: x*y, [10,20,30,40,50]))


# import functools
# print(functools.reduce(lambda x,y: x+y, ['a','b','c','d'], 'z='))


# # факториал
# import functools
# s = int(input("Введите цифру: "))
# def mul(x, y):
#     return x*y
# print(functools.reduce(mul, range(2, s+1),1))


# Пересмотри 8-ой урок! ????????????????????????????????????????????????
# from functools import cmp_to_key
# def mul(x,y):
#     if x > y: return 1
#     elif x == y: return 0
#     else: return -1
# print(sorted([1,0,-1,3,4], key = cmp_to_key(mul)))
# Эта функция по идее должна заходить в [] и и подставляет (сравнивает?) x и y так,
# чтобы равенство было правильным и только потом выводит


# # Комбинаторика
# import itertools
# for k in itertools.combinations([1,2,3,1], 2):
#     print(k)
# print()
# for k in itertools.combinations([1,2,3,1], 3):
#     print(k)
# print()
# for k in itertools.combinations([1,2,3,1], 5):
#     print(k)
# 1,2,3 and 3,2,1 are the same for the code
# Выше без повторений, ниже с повторениями
# import itertools
# for k in itertools.combinations_with_replacement([1,2,3,1], 3):
#     print(k)


# # Задача с монетками
# import itertools
# tes1 = set()
# for k in itertools.combinations([1,1,2,2,5,5,10,10], 2):
#     # print(k)
#     tes1.add(sum(k))
# print(tes1)


# import itertools
# tes2 = set()
# for k in itertools.combinations([1,2,5,10]*2, 2):
#     # print(k)
#     tes2.add(sum(k))
# print(tes2)


# Try Except:


# # ValueError:
# while True:
#     try:
#         a = int(input())
#         print(a)
#         if a == 0: break
#     except ValueError:
#         print('Open your eyes!')


# # IndexError:
# a = [1,2,3,4]
# try:
#     print(a[-5])
# except IndexError:
#     print('***')


# По приколу три раза:
# for i in '123':
#     print(f'Попытка {i}')
#     try:
#         s = input('--->')
#         f = open(s)
#         print(f'Файл {s} не найден!')
#     except FileNotFoundError:
#         print(f'Файл {s} не найден!')


# # Функция генератор:
# def fun(n):
#     for x in range(n):
#         print('ДО:', x)
#         yield x * x
#         print('ПОСЛЕ:', x)
# g = fun(3)
# # print(type(g))
# for k in g:
#     print('Перед печатью: ')
#     print(f"{k = }")

# print()

# def fun(n):
#     for x in [10,20,30]:
#         print('ДО:', x)
#         yield x * x
#         print('ПОСЛЕ:', x)
# g = fun(3)
# for k in g:
#     print('Перед печатью: ')
#     print(f"{k = }")


# def fun(n):
#     for x in range(n):
#         if x % 2 == 0:
#             yield x * x
#         else:
#             yield x ** x
# g = fun(8)
# for k in g:
#     print(f'{k = }')

# т.е. тут 0 заходит в проверку - выдает ноль - мы печататем ноль
# потом берем единицу (всего 8 проверок) и подставляем в yield - нечетное - возводим в степень 3 = 1 - выводим
# потом берем двойку - проверяем в yield - четное - умножаем на два = 4
# потом берем 3 - поверяем четное или нет в yield - нечетное - возводим в третью степень - итого 27
# затем берем 4 - проеряем в yield - четное, возводим в квадрат - 16 - возвращаемся вниз и печатаем 16


# return - оператор выводит только одно значение
# yield - возвращает серию результатов
# and so on


# ????????????????????????????????????????????????????????????????
# def fun(n):
#     for x in range(n):
#         if x % 2 == 0:
#             yield x*x
#         else:
#             yield x**3
# g = fun(3)

# for k in range(10):
#     try:
#         print(next(g))
#     except StopIteration:
#         print('Конец!')
#         break

# next выдает следующее
# можно обойтись и без него for k in j....

# def fact (n):
#     f, k = 1, 1
#     while True:
#         yield f
#         k += 1
#         if k > 10:
#             return
#         f *= k
# gen_fact = fact(10)
# for m in gen_fact:
#     print(m)


# def fact():
#     f, k = 1, 1
#     while True:
#         print(k, end=' ')
#         yield f
#         k += 1
#         f *= k
# gf = fact()
# while True:
#     print(next(gf))
#     input()
# # Каждый раз когда мы нажимаем на play то код выполняется


# lst = [1, 2, 4, 8, 16, 32]
# def sum_firsts():
#     s = 0
#     for i in lst:
#         s += i
#         yield s
# gf = sum_firsts()
# for k in gf:
#     print(k)


# ???????????????????????? ЧТО ТУТ НАХОЙ ПРОИСХОДИТ!!!!?????
def f123():
    n = 1
    while True:
        for i in range(n):
            yield n
        n += 1


gf = f123()
for i in range(10):
    print(next(gf), end=' ')
