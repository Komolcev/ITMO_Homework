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


# # # Задание 6-2:
# first = set(input("Введите элементы через пробел и запятую: ").split(", "))
# second = set(input("Введите элементы через пробел и запятую: ").split(", "))
# print(len(first & second))


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