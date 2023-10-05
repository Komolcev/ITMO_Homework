# # Фильтр
# def chet(x):
#     if x%2:return False
#     return True
# print(list(filter(chet, {0,1,2,3,4,5,6,7,8,9})))


# def less_5(x):
#     if x < 5: return True
#     return False
# print(list(filter(less_5, {0,1,2,3,4,5,6,7,8,9})))


# s = list(map(int, input().split()))
# s,x,z = print(map(int, ['1','2','3']))
# sorted('abdsfssrgl')
# print(sorted([1, 2, 3, 4, 5, 0, 9]))


# def quad(x):
#     return x * x
# print(sorted([14,1,5,2,10], key = quad))


# sorted_list = sorted(['123','b','klm','12334', '1', '22', 'a'], key = len)
# print(sorted_list)


# def quad(x):
#     return -x * x
# print(sorted ([1,-2,3,-4,5], key = quad))


# from math import * # Everything
# print(lcm(24,36,48))
# print(gcd(24,36,48))


# from math import pi
# def circle_area(r):
#     return(pi*r**2)
# r = float(input())
# print(circle_area(r))


# def circle_area(d):
#     from math import pi
#     return pi * d ** 2 / 4
# d = float(input())
# print(circle_area(d))


# import numpy as np
# import pandas as pd
# потом будет использоваться как np.


# help('modules')
# medium статьи хорошие почитать

# crt = [(1,2),(0,2),(1,1),(1,0),(0,3))]
# print(sorted(crt))


# crt = [(1, 2), (0, 2), (1, 1), (1, 0), (0, 3), (2, 2)]
# def s(x):
#     return x[0], -x[1]
# print(sorted(crt, key = s))


# crt = [(1, 2), (0, 2), (1, 1), (1, 0), (0, 3), (2, 2)]
# def s(x):
#     return -x[0], -x[1]
# print(sorted(crt, key = s))


# crt = [(1, 2), (0, 2), (1, 1), (1, 0), (0, 3), (2, 2)]
# def s(x):
#     return -x[1], -x[0]
# print(sorted(crt, key = s))


# crt = [(1, 2), (0, 2), (1, 1), (1, 0), (0, 3), (2, 2)]
# def s(x):
#     return x[1] + x[0]
# print(sorted(crt, key = s))


# IMPORTANT!
# x = 5
# print(eval('x * 5'))
# print(eval('abs(-123)'))
# y = 10
# print(eval('x * y'))


# IMPORTANT!
# x = 10
# y = 5
# def f(x):
#     return x + y
# print(eval('f(x)'))


# x = 'a = 15'
# exec(x)
# print(a)


# # IMPORTANT!
# def f(x): return x % 10
# print(sorted([123,12,11,30], key = f))

# Эквивалентно:

# print(sorted([123,12,11,30,16,63], key = lambda x: x % 10))
