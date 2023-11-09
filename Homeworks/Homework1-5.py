# # Задача 1-1
# a = int(input('Введите число: '))
# b = int(input('Введите число: '))
# c = a + b
# d = a * b
# print('Сумма a и b = ', c)
# print('Произведение a и b = ', d)


# # Задача 1-2
# a = float(input('Введите число: '))
# b = float(input('Введите число: '))
# c = a + b
# d = a - b
# e = a * b
# f = a / b
# g = a // b
# if c >= d and c >= e and c >= f and c >= g:
#     print("Наибольшее число: ", c)
# elif d >= c and d >= e and d >= f and d >= g:
#     print("Наибольшее число: ", d)
# elif e >= c and e >= d and e >= f and e >= g:
#     print("Наибольшее число: ", e)
# elif f >= c and f >= d and f >= e and f >= g:
#     print("Наибольшее число: ", f)
# else:
#     print("Наибольшее число: ", g)


# # Задача 1-3
# x, y = float(input('Введите число 1: ')), float(input('Введите число 2: '))
# a, b, c, d, e = x+y, x-y, x*y, x/y, x//y
# cur_max1, cur_max2 = a, b
# if a < b:
#     cur_max1, cur_max2 = b, a
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
# print("Наибольшее число 1: ", cur_max1, "Наибольшее число 2: ", cur_max2)


# # Задача 2-1:
# a = int(input('Введите число: '))
# for i in range(1, 10+1):
#     b = a * i
#     print(str(a) + ' x ' + str(i) + ' = ' + str(b))


# # Задача 2-2:
# lst = input("Введите цифры через пробел: ").split()
# min_num = int(lst[0])
# for num in lst:
#     if int(num) < min_num:
#         min_num = int(num)
# print("Наименьшее число в списке: ", min_num)


# # Задача 2-3:
# n = int(input("Введите число: "))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
# print("Факториал числа", n, "равен", factorial)


# # Задача 3-1:
# summa = 0
# counter = 0
# while True:
#     a = int(input('Введите зарплаты сотрудников, окончание ввода -> 0: '))
#     if a == 0:
#         break
#     summa += a
#     counter += 1
# print('Средняя зарплата сотрудников: ', summa/counter)


# #  Задача 3-2:
# a = input('Введите число: ')
# digits_count = [0] * 10
# for digit in a:
#     digits_count[int(digit)] += 1
# for i in range(10):
#     print(f"Цифра {i}: {digits_count[i]}")


# #  Задача 3-3:
# sentence = input("Введите предложение: ")
# arr1 = sentence.split()
# max_length = 0
# for word in arr1:
#     word_length = len(word)
#     if word_length > max_length:
#         max_length = word_length
# print(max_length)


# # Задача 4-1:
# arr1 = str(input(
#     'Введите два числа и математ. действие (+, -, * или /) через пробел: ')).split()
# b = float(arr1[0])
# c = float(arr1[2])
# if arr1[1] == '*':
#     d = b * c
#     print('Умножение двух чисел равно:', + d)
# elif arr1[1] == '+':
#     d = b + c
#     print('Сложение двух чисел равно:', + d)
# elif arr1[1] == '-':
#     d = b - c
#     print('Вычитание двух чисел равно:', + d)
# elif arr1[1] == '/' or arr1[1] == ':':
#     if b == 0:
#         print('На ноль делить нельзя!')
#     else:
#         d = b / c
#         e = round(d, 2)
#         print('Деление двух чисел равно:', + e)
# else:
#     print('Что-то пошло не так, попробуйте еще раз!')


# # Правильное решение 4-1:
# s = input().split()
# a, b = int(s[0]), int(s[2])
# if s[1] == '+':
#     print(a + b)
# elif s[1] == '-':
#     print(a - b)
# # ...


# # Задача 4-2:
# # Получаем число n
# n = int(input("Введите число: "))

# # Возводим число в квадрат
# n_square = n ** 2

# # Кладем в массив arr1 все числа, от 1 до n**2
# arr1 = [x for x in range(1, n_square + 1)]

# # Создаем матрицу n на n, заполненную нулями
# matrix = [[0] * n for _ in range(n)]

# # Инициализируем переменные для координат текущей позиции
# row = 0  # Ряд
# col = 0  # Колонка

# # Инициализируем переменные для изменения направления движения по матрице
# dir_row = 0  # Направление ряда
# dir_col = 1  # Направление колонки

# # Заполняем матрицу. Этот код заполняет элемент матрицы с индексами [row][col]
# # значением из списка arr1. При каждой итерации цикла, значение из списка arr1
# # присваивается переменной num. Затем это значение присваивается элементу матрицы с индексами [row][col].
# for num in arr1:
#     matrix[row][col] = num

#     # Проверяем, нужно ли изменить направление движения
#     if row + dir_row == n or col + dir_col == n or row + dir_row < 0 or col + dir_col < 0 or matrix[row + dir_row][col + dir_col] != 0:
#         dir_row, dir_col = dir_col, -dir_row

#     # Обновляем координаты текущей позиции
#     row += dir_row
#     col += dir_col

# # Выводим матрицу
# for row in matrix:
#     print(row)


# # Еще одно решение 4-2:
# n = int(input())
# m = {}
# for i in range(n):
#     for j in range(n):
#         m[i, j] = 0
# x, y, dx, dy = 0, 0, 0, 1

# for k in range(1, n * n + 1):
#     m[x, y] = k
#     # print(k, x, y, m[x, y])
#     if m.get((x + dx, y + dy), -1) != 0:
#         if (dx, dy) == (0, 1):
#             dx = 1
#             dy = 0
#         elif (dx, dy) == (1, 0):
#             dx = 0
#             dy = -1
#         elif (dx, dy) == (0, -1):
#             dx = -1
#             dy = 0
#         elif (dx, dy) == (-1, 0):
#             dx = 0
#             dy = 1
#     x += dx
#     y += dy

# len_nn = len(str(n*n))

# for i in range(n):
#     for j in range(n):
#         print(f"{m[i,j]:{len_nn}}", end=' ')
#     print()


# # Задача 4-3:
# sentence = input(str('Введите предложение, которое разделяется точкой: '))
# sentences = sentence.split(".")
# array1 = []
# array2 = []

# # Вставляем в массив array1 все, что до точки, если это буква, в нижнем регистре
# for char in sentences[0]:
#     if char.isalpha():
#         array1.append(char.lower())

# # То же самое для второго предложения
# for char in sentences[1]:
#     if char.isalpha():
#         array2.append(char.lower())

# # Создаем два словаря
# counter1 = {}
# counter2 = {}

# # Проходимся по каждой букве в array1 и записываем количество
# for letter in array1:
#     if letter in counter1:
#         counter1[letter] += 1
#     else:
#         counter1[letter] = 1

# # Проходимся по каждой букве в array2 и записываем количество
# for letter in array2:
#     if letter in counter2:
#         counter2[letter] += 1
#     else:
#         counter2[letter] = 1

# # Сравниваем словари
# if counter1 == counter2:
#     print(True)
# else:
#     print(False)


# # еще один вариант 4-3:
# s1 = input()
# s2 = input()
# ab = 'sdasdasdasdasd2342hjash4ew'
# ds1, ds2 = {}, {}
# for i in s1.lower():
#     if i in ab:
#         ds1[i] = ds1.get(i, 0) + 1
# for i in s2.lower():
#     if i in ab:
#         ds2[i] = ds2.get(i, 0) + 1
# print(ds1 == ds2)


# # Задание 5-1:
# n = int(input("Введите количество строк треугольника Паскаля: "))
# triangle = []
# for i in range(n):
#     row = []
#     row.append(1) # в ряд вставь единицу
#     if i != 0: # тут осущ-ся проверка для первой единицы (иначе не печатается)
#         for j in range(i - 1): # пройтись по всем элементам, кроме первого и последнего
#             row.append(triangle[i - 1][j] + triangle[i - 1][j + 1]) # добавляем в ячейку сумму двух чисел из предыдущей строки
#         row.append(1) # добавь единицу в конец ряда
#     triangle.append(row)
#     print(', '.join(map(str, row)))


# # Задание 5-2:
# n = int(input())
# arr1 = []
# # Проверяем целое число или нет и сортируем их
# for i in range(1, int(n ** 0.5) + 1):
#     if n % i == 0:
#         arr1.append(i)
#         arr1.append(n // i)
#         arr1.sort()
# print(*arr1)

# # Тут темный лес :-(
# k = 2
# while k <= n:
#     if n % k == 0:
#         count = 0
#         while n % k == 0:
#             count += 1
#             n //= k
#         print(f"{k}-{count}")
#     k += 1


# # Задание 5-3:
# n = int(input('Введите число, отличное от 0: '))
# arr1 = []

# if n == 0:
#     print('1')
# if n == 1:
#     print('1')

# else:
#     arr1 = [1, 1]
#     for i in range(2, n + 1):
#         arr1.append(arr1[i - 1] + arr1[i - 2])

# print(" ".join(map(str, arr1)))
# end = " "


# shif + option + f = все с пробелами!


# # Задание 6-1:
# lst = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XC': 90, 'XL': 40, 'CD': 400, 'CM': 900}

# def conv(x):
#     counter = 0
#     while len(x) > 0:
#         if x[:2] in lst:
#             counter += lst[x[:2]]
#             x = x[2:]
#         else:
#             counter += lst[x[0]]
#             x = x[1:]
#     return counter

# x = str(input())
# print(conv(x))


# # Задание 6-2:
# first = set(input().split())
# second = set(input().split())
# intersection = first.intersection(second)
# print(len(intersection))


# # Задание 6-3:
# def symbol(s):
#     arr1 = []
#     arr2 = []
#     arr3 = []
#     for i in s:
#         if i.isdigit() == True:
#             arr1.append(i)
#         elif i.isalpha() == True:
#             arr2.append(i)
#         else:
#             arr3.append(i)
#     return arr1, arr2, arr3

# s = str(input())
# vivod = symbol(s)
# for i in vivod:
#     print(*(sorted(set(i))))
