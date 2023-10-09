# print(print(123))
# None

# print(print)

# Last homework
# x, y = int(input()), int(input())
# print(x*y, x*y)

# x, y = int(input()), int(input())
# a,b,c,d,e = x+y, x-y, x*y, x/y, x//y
# print(a,b,c,d,e)
# cur_max1, cur_max2 = a, b
# if a < b: cur_max1, cur_max2 = b, a

# if c > cur_max1:
#     cur_max1, cur_max2 = c, cur_max1
# elif c > cur_max2:
#     cur_max2 = c

# if d > cur_max1:
#     cur_max1, cur_max2 = d, cur_max1
# elif d > cur_max2:
#     cur_max2 = d

# if e > cur_max1:
#     cur_max1, cur_max2 = e, cur_max1
# elif e > cur_max2:
#     cur_max2 = e

# print(cur_max1, cur_max2)

# print(1,2,3, sep = ':')
# print(4,5,6, end = '*')
# print(7,8,9, end = '\n')

# for i in 'Hello World!':
#     print(i, end='') # в строку

# for i in 'Hello World!':
#     print(i, end='.')

# for i in 'Hello, world!':
#     j = i + i
#     print(j, end='_')

# import math
# print(math.pi, math.e)

# i = int(input())
# for i in range(10):
#     if i % 2 == 1:
#         print(f"{i} - нечетное")
#     else:
#         print(f"{i} - четное")


# j = int(input('Введите число: '))
# for i in range(1, j+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)


# for i in 'Hello World!':
#     if i == 'o':
#         continue
#     print(i * 2, end='')


# for i in range(int(input())):
#     if i > 10: break
#     if i % 2 : continue
#     print(i)

# Типы
# # tuple - кортеж
# c = (123)
# print(type(c))

# a = '123'
# print(type(a))

# b = [1,2,3]
# print(type(b))


# # Срезы
# s = 'Война и мир'
# print(s[::-1])
# # print(s[начальное:конечное:шаг])


# s = 'Война и мир'
# print(s[::-1])
# len(s)
# z = s[:6] + 'and' + s[7:]
# print(z)


# n = int(input('Введите число: '))
# for i in range (1, n + 1):
#     for _ in range (i):
#         print('*', end = '')
#     else:
#         print()


# n = int(input('Введите число: '))
# for i in range (1, n + 1):
#     print('*' * i)


# # Список
# lst = [1,33,'abc',5,22,True,[123]]
# lst[1] = 777 #Меняем второй элемент
# print(lst)
# print(len(lst), 'Длина')

# lst = list()
# print(lst)
# print(len(lst))

# #mutable - изменяемый
# lst = ['hello', 1, 2, True]
# print(lst[1],lst[2])
# print(len(lst))

# # Значение индекса и порядковый номер индекса
# lst = [1,5,2,4,6]
# for i in range(len(lst)):
#     print(i, lst[i])

# # Новый способ распечатать порядковый номер и значение
# lst = [1,5,2,4,6]
# for i, j in enumerate(lst):
#     print(i, j)


# lst = [10, 'aa', 20, 'MMM']
# for i in lst:
#     if type(i) == str:
#         print(i * 2)
#     elif type(i) == int:
#         print(i ** 2)
# lst.append('FGH')
# print(lst)

# lst1 = []
# for i in range(5):
#     lst1.append(i)
# print(lst1)

# a=[1,2,3,4,5]
# b = []
# s = 0
# for i in a:
#     s += i
#     b.append(s)
# print(b)

# print(sum(lst))
