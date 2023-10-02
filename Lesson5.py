# abc = {1: '1', '1': 1}
# for k, v in abc.items():
#     print(k, v)


# nums = [0,1,2,3,4,5]
# nums.append(nums[:])
# print(nums)
# print(len(nums))


# data = {tuple(): 1}
# print(data)


# ключем не может быть словарь и список и любые изменяемые элементы!


# import string
# print(*string.ascii_letters)
# print(*string.digits)
# print(dir(string))
# print(*string.whitespace)


# tpl = (1,50,123,234,333,456,500,555,678,890,900,912,999,1000)
# n = int(input())

# if n <= tpl[0]:
#     res = (n,) + tpl
# elif n >= tpl[-1]:
#     res = tpl + (n,)
# else:
#     for i in range(len(tpl) - 1):
#         if tpl[i] <= n <= tpl[i+1]:
#             res = tpl[:i+1] + (n,) + tpl[i+i:]
#             break
# print(res)


# cdt = {1:111, 2:222, 3:333}
# print(cdt.get(3, 444))
# print(cdt)
# # не меняет словарь!
# print(cdt.setdefault(5, 555))
# print(cdt)
# # меняет словарь!


# n = int(input('Количество пар: '))
# syn = {}

# for i in range(n):
#     s = input('Два синонима: ').split()
#     syn[s[0]] = s[1]
#     syn[s[1]] = s[0]

# while True:
#     p = input('Введите слово для выхода exit или введите одно из пар: ')
#     if p == 'exit':
#         break
#     print(syn.get(p.lower()))


# dct = {1:111, 2:222}
# for key, value in dct.items():
#     print(key, value)
# x = dct.items()
# print(x)


# dct = {1:111, 2:222}
# for key, value in dct.items():
#     print(key, value)
# x = dct.items()
# print(x)
# dct[3] = 333
# print(x)


# lst = list(map(int, input().split()))
# # все что введешь, то будет в lst
# print(lst)


# lst = list(map(int, input().split()))
# dct = {}
# # dct = словарь
# for i,j in enumerate(lst):
#     if j in dct:
#         dct[j].append(i)
#     else:
#         dct[j] = [i]
# print(dct)


# dct = {1:123, 2:222}
# for i in dct.items():
#     print(i, type(i))


# dct = {1:123, 2:222, 3:333, 5:555}
# for i in dct.items():
#     print(f"{i=} {dct[1]=} {dct[3]=}")


# dct = {1:111, 2:222}
# tcd = {2:333, 4:444}
# dct.update(tcd)
# print(dct)


# # Например, напиши груши 100, яблоко 200:
# # Окончание 0
# sales_report = {}
# while True:
#     s = input('')
#     if s == '0': break
#     p = s.split()
#     if p[0] not in sales_report:
#         sales_report[p[0]] = 0
#     sales_report[p[0]] += int(p[1])
# # print(sales_report)
# for i, j in sales_report.items():
#     print(i,j)


# print(divmod(21,4))
# # целый результат, второе число - остаток


# print(round(1.1234567, 4))


# print(round(4.5))
# print(round(3.5))
# print(round(2.5))
# print(round(1.5))
# # округление вверх или вниз в зависимости от того честное или нечетное число


# f = float(input())
# print(f)


# import math
# a = float('inf')
# print(a)
# print(a * 2)
# type(a)
# print(math.inf)


# for i in range(16):
#     print(i, bin(i), hex(i))


# print(int('10', 16))


# sec = int(input())

# a = int(input())
# print(a)
