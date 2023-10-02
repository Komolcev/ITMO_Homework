# dct = {1:111}
# k = 0
# dct.get(k)


# dct = {1:111, 2:222, 3:333}
# k = 2
# print(dct.pop(k))
# print(dct)


# dct = {1:11, 2:22, 3:33}
# print(dct.popitem())
# print(dct)


# # Сортировка
# dct = {1:11, 2:22, 3:33}
# print(sorted(dct, reverse = True))


# x = True
# print(True + i)
# print(str(x))
# print(x)
# # !!! т.к. True = 1 !!!
# x = True
# print(True + True)


# # Цифры и буквы
# print(ord('A'))
# print(chr(1040))
# for i in range(1040, 1040+32):
#     print(chr(i), end='')
# print()
# print(chr(1072+33))
# print(ord('ё'), ord('Ё'))
# print(chr(20320))
# # "Ты"


# ord_a = ord('A')
# for i in range(ord_a, ord_a + 26):
#     print(i, chr(i))


# 'a' < 'b' == True


# 'aaabcde' < 'aabbcde' == True


# a = [1, 2, 3]
# b = a
# a == b #True
# a is b #Ture


# a = [1, 2, 3]
# b = [1, 2, 3]
# a == b #True
# a is b #False


# x = 10
# y = 20
# if x > y or y / 0:
#     print('111') #print 111


# x = 10
# y = 20
# if x > y and y / 0:
#     print('111') #error / 0


# if lst: # if len(lst)>0


# god = int(input())
# if god % 4 == 0 and god % 100 != 0 or god % 400 == 0:
#     print('yes')
# else:
#     print('no')


# # Гласные и согласные чередует программа 1
# s = input()
# v, c, res = [], [], ''
# for letter in s:
#     if letter in 'aeiou':
#         v.append(letter)
#     else:
#         c.append(letter)
# if abs(len(v) - len(c)) > 1:
#     print('Impossible!')
# else:
#     if len(v) == len(c):
#         for i in range(len(v)):
#             res += c[i] + v[i]
#     elif len(v) < len(c):
#         for i in range(len(v)):
#             res += c[i] + v[i]
#         res += c[-1]
#     else:
#         for i in range(len(c)):
#             res += v[i] + c[i]
#         res += v[-1]
# print(res)


# # Гласные и согласные чередует программа 2 ZIP
# s = input()
# v, c, res = [], [], ''
# for letter in s:
#     if letter in 'aeiou':
#         v.append(letter)
#     else:
#         c.append(letter)
# if abs(len(v) - len(c)) > 1:
#     print('Impossible!')
# else:
#     for i, j in zip(c,v):
#         res += i + j
# print(res)


# a = set([1,2,3, 1, 0, -1, False, True])
# print(a, type(a))
# # False and 1 is already there!
# len(a)


# a = set([1,2.0,3,0,-1,2,(1,2,3),'123'])
# print(a, type(a))
# # -2 is already there!
# len(a)


# lst = [1,2,2,3,3,3,4,4,4,4]
# lst = 'aaaafffffftttttvvd'
# tes = set(lst)
# print(len(set(lst)))
# print(len(set(lst)))


# lst = []
# dct = {}
# st = ''
# sss = set()
# type(sss)


# months = {'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec',}
# print(sorted(months))
# # sorted из всего делает список
# print(months)
# print('May' in months)


# tes = set(map(int, input().split))
# print(tes)
# print(sum(tes)/len(tes))


# tes = set(1,2,3)
# print(tes)
# tes.add(4)
# print(tes)


# # сколько букв в введенной строке
# s = input()
# tes = set(s)
# print(tes)
# if len(tes) == 33:
#     print(True)
# else:
#     print(False)


# a = {1,2,3,4,5,6,7,8,9}
# b = {4,5,6,7,8,0}
# print(a - b)
# print(a ^ b)
# #  ^ - встречаются 1 раз


# # уникальные элементы
# lst = ['мама', 'мыла', 'раму']
# res = set()
# for i in lst:
#     res |= set(i)
# print(res)
# # есть еще фроузен сет - его нельзя изменить


# def convert_to_fhr(temp):
#     result = (9/5) * (temp+32)
#     return result

# x = convert_to_fhr(18)
# print(x)
