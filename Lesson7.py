# print({1,2,3,(1,2,3),"123",1.0})
# print(({1,2,3,4,5,'1,2,3'}).pop())
# print(({1,2,3,4,5,'123',(1,2,3)}).add(1))


# tes = {1,2,3,4,5, '123', (1,2,3)}
# print(tes.add(1))
# print(tes)


# Множества были 2-3 урока назад, если что
# То, что лежит во множестве, не повторяется
# Объявляются в круглых скобках


# [] - массив
# () - кортеж = tuple
# {} - словарь
# () - множество = set


# def pod_nalog(dokhod):
#     result = int(dochod * 0.13)
#     return result


# while True:
#     dochod = int(input('Введите значение: '))
#     if dochod == 0: break
#     print(dochod, pod_nalog(dochod))


# def pod_nalog(dokhod, percent = 13):
#     result = dokhod * percent / 100
#     return result


# while True:
#     dokhod1 = float(input('Введите: '))
#     percent1 = float(input('Введите: '))
#     if dokhod1 <= 0: break
#     print(dokhod1, pod_nalog(dokhod1, percent1))
#     print(dokhod1, pod_nalog(dokhod1))


# def my_function(arg1, arg2, *args):
#     print (arg1, arg2)
#     for i in args:
#         print(i)
# my_function(123, 111, 333, 555, 777, 999)


# # Функция, принимающая много аргументов!
# def multi(*args):
#     res = 1
#     for i in args:
#         res *= i
#     return res
# print(multi(100, 200))


# def multi(**kwargs):
#     print(kwargs)
#     res = 1
#     for i, j in kwargs.items():
#         if isinstance(j, int):
#             res *= j
#     return res
# print(multi(a = 100, b = 200))
# Эта функция принимает произвольное количество именованных аргументов.
# Она выводит переданные аргументы на экран и затем перемножает все целочисленные аргументы,
# возвращая полученное произведение. В данном случае, функция принимает аргументы "a" со значением
# 100 и "b" со значением 200, выводит их на экран и возвращает их произведение, то есть 100 * 200 = 20 000


# def multi(**kwargs):
#     # print(kwargs)
#     res1 = 1
#     res2 = ''
#     for j in kwargs.values():
#         if type(j) == int:
#             res1 *= j
#         elif type(j) == str:
#             res2 += j
#         else:
#             print(j)
#     return res1, res2

# print(multi(a = 100, b = '200', c = 5.4, d = 'y', e = [1,2,3]))


# def all_args(var1, *args, **kwargs):
#     print(var1)
#     print(args)
#     print(kwargs)

# all_args(1, 2, 3, x = 100, y = 200)


# def all_args(var1, *args, **kwargs):
#     print(var1)
#     print(args)
#     print(kwargs)

# all_args(1, x = 100, y = 200)


# def all_args(var1, *args, **kwargs):
#     print(var1)
#     print(args)
#     print(kwargs)

# all_args(1)


# def nalog(dochod, *args):
#     for i in args:
#         print(int(dochod * i / 100))
#     return
# x = int(input())
# print(nalog (x, 13, 15, 20))
# # (от 100 - 13, 15, 20)


# def uni_let(lst):
#     s = ''.join(lst)
#     string = ''.join(sorted(set(s)))
#     return string, len(string)


# print(uni_let(['All', 'you', 'need', "is", 'love']))
# print(uni_let(['AbracadabrA']))


# def function(n):
#     def function1(p):
#         return p*p
#     def function2(w):
#         return w*w
#     if n < 10:
#         p = n
#         return function1(p)
#     else:
#         w = n
#         return function2(w)
# n = int(input('Введите число: '))
# print(function(n))


# n = int(input())
# print(function(n))
