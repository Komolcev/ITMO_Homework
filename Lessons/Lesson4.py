# # ищет слева
# s = 'abrakadabra'
# for k in s:
#     print(k, s.find(k))

# # ищет справа
# s = 'abrakadabra'
# for k in s:
#     print(k, s.rfind(k))

# lang = 'Python'
# print(f'{lang} is the best!')

# print(' All you need is love! '.split())

# print(' All you need is love! '.split(' '))
# # некрасивая штука, но иногда нужная

# s = input().split()
# # вводим и сразу делим на слова


# x, y, z = 0, 0, 0
# cor1 = (x, y, z)
# cor1 = 100, 200, 300
# print(x, y, z)


# # Не работает!?
# cort = (123,234,345,456,567,678,789,890)
# n = int(input())
# for i,j in enumerate(cort):
#     print(i, j)
# cort1 = cort[:index] + tuple((n,)) + cort[index:]
# print(cort1)


# cort = (123,234,345,456,567,678,789,890)
# n = int(input())
# index = 0
# for i,j in enumerate(cort):
#     if n > j: index = 1
#     else: break
# cort1 = cort[:index] + tuple((n,)) + cort[index:]
# print(cort1)


# # не успел
# tpl = (1,2,3,[11,22,33])
# tpl[3].append(44)
# ...

# How does it work???
# tpl = (1,2,3,[11,22,33])
# a = 2 * tpl
# print(a)


# # Словарь:
# hm = {}
# s = input()
# for k in s:
#     if k not in hm:
#         hm[k] = 0
#     hm[k] += 1
#     print(hm)
#     input()


# hm = {}
# s = input()
# for k in s:
#     if k not in hm:
#         hm[k] = 0
#     hm[k] += 1
# for k in hm:
#     print(k, hm[k])

# s = input()
# dct = {}
# for k in s:
#     if k not in dct:
#         dct[k] = 0
#     dct[k] = dct[k] + 1
# print(dct)

# s = input()
# dct = {}
# for k in s:
#     j = int(k)
#     if j not in dct:
#         dct[j] = 0
#     dct[j] = dct[j] + 1
# print(dct)


# s = {}
# s['Name'] = 'Sergei'
# s['Surname'] = 'Komolcev'
# s['Mail'] = 'ser-komolcev@yandex.ru'
# s['Name'] = 'Alex'
# s['Mail'] = True
# print(s)
# print(s['Name'])
# for k in s:
#     print(k)
#     print(k, s[k])


# dct = {}
# while True:
#     s = input()
#     if s == '0':
#         break
#     if s in dct:
#         dct[s] += 1
#     else:
#         dct[s] = 1
# print(dct)


# dct = {1:'Один', 2:'Два', 3:'Три'}
# s = input()
# for i in s:
#     print(dct[int(i)], end='')

# a = dict(name = 'маша', age = '16')
# print(a)

# a = [111, 222, 333]
# b = ['aaa', 'bbb', 'ccc']
# c = dict(zip(a, b))
# print(c)


# month = {1:31, 2:28, 3: 31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
# while True:
#     y = int(input())
#     m = int(input())
#     if y == 0: break
#     print(month[m])


# s = input().split()
# dct = {}
# for i in s:
#     if i in dct:
#         dct[i] += 1
#     else:
#         dct[i] = 1
# ml = min(dct.values())
# for i in dct:
#     if dct[i] == ml:
#         print(i, end=' ')


# dct = {1:11, 2:22}
# x = 1
# print(dct.get(x, 0))
# x = 2
# print(dct.get(x, 0))
# x = 3
# print(dct.get(x, 0))
# x = 11
# print(x in dct.values())


# if x in dct:
#     print(dct[x])
# else:
#     print(0)
# # get не меняет словарь!


# s = input()
# dct = {}
# for k in s:
#     dct[k] = dct.get(k, 0) + 1
#     print(dct)


# s = input()
# dct = {}
# for k in s:
#     dct[k] = dct.get(k, '') + k
# print(dct)


# # Проверка на анаграммность
# p, q = input().split()
# pp, qq = {}, {}
# for i in p:
#     pp[i] = pp.get(i, 0) + 1
# for i in q:
#     qq[i] = qq.get(i, 0) + 1
# print(pp == qq)


# Важная задача на словари
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
