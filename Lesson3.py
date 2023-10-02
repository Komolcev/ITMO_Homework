# x = '1,2,3'
# print(type(x))
# for i in x:
#     print(i)

# x = '1,2,3'
# print(type(x))
# for i in x:
#     print(i, end = '')

# for i in range(10):
#     if i == 5: break
#     else: print(i, end = '')
# else:
#     print('Here!')

# for i in range(10):
#     if i == -5: break
#     else: print(i, end = '')
# else:
#     print('Here!')

# list = [-1,2,3,0,5,-2,0,10,12,-6,-5,-10]
# cur_min = list[0]
# second_min = int
# for i, j in enumerate(list):
#     if j < cur_min:
#         cur_min = j
# for i, j in enumerate(list):
#     if cur_min < j < second_min:
#         second_min = j
# print("Второе минимальное значение: ", second_min)

# n = int(input())
# f = 1
# for i in range(1, n + 1):
#     f * =i
# print(f)

# n = 123
# s = 'abc'
# print(f"{n:08}__{s:*<5}")

# # !!!!!range = индесы!!!!
# # Без range идет по
# arr1 = [[1,2,3],[4,5,6],[7,8,9]]
# summa = 0
# for i in arr1:
#     for j in i:
#         summa += j
# print('Сумма:', summa)

# Когда ты используешь i in range, в будущем тебу придется обращаться к элементу с индексом i
# a = [5, 7, 9]
# for i in range(0, len(a)): —— i каждый раз бдет меняться и будет 0, 1, 2
#     print(a[i]) —— программа каждый раз будет выводить элементы массива а, так как ты обращаешься к элемменту с индексом каждый раз на еденицу больш
#     print(i) ——— программа выведет 1 2 3


# когда ты используешь i in a, то идешь по эллементам в массиве, А НЕ ПО ИНДЕКСАМ
# for i in a:
#     print(i) —— программа выведет 5 7 9, тк мы идем по эллементам
#     при попытке print(a[i]) выдаст ошибку
# Это может сработать, например, если
# a = [2, 7, 5]
# for i in a:
# print(a[i])
# для первого захода в цикл i  будет равен 2, тогда принт выдаст эллемент a с индексом 2, а он равен 5


# arr1 = [[1,2,3],1000,[4,5,6],2000,[7,8,9],333]
# summa = 0
# for i in arr1:
#     # print(i, type(i))
#     if type(i) == list:
#         for j in i:
#             summa = summa + j
#     else:
#             summa = summa + i
# print(summa)



# s = 'abbcccddddeeeee ffffff1234567821231223123'
# for i in s[::-2]:
#     print(i, end = '')
# print(s[-1])
# print(s[-31])
# print(s[len(s)-1])



# shift + option + down = the copy of the line!!!!!!!



# s = 'Abra cad abra'
# print('abr' in s)
# print(s.find('abr'))
# print(s.find('cad'))
# print(s.find(' '))
# print(len(s))
# print(s.count('a'))
# print(s.count('a'))
# for i in s:
#     print(i, i.islower())

# s = '1234sdfdsf' ?

# s = 'abra cad abra'
# print(s.split())

# x = 'abra cad abra'
# x.split()  # Он тут не запоминает что он сделал
# print(x)

# lst = ['Я','пишу','на','Python']
# tsl = ' '.join(lst)
# print('\n'.join(lst))
# print(tsl.split())

# s = 'я Вам пишу. чего же боле. Что я могу еще сказать?'
# p = s.split('.')
# for i in p:
#     print(i. split())


# print(list('abcdef'))
# print(['a','b','c','d','e','f'])
# print([1, 2, 3])
# a = [1,2,3,4,5,6,7]
# a.append(0)
# a.sort()
# print(a)
# sorted(a, reverse = True)


# arr1 = []
# n = 10
# for i in range(1, n+1):
#     for j in range(i):
#         arr1.append(i)
# print(arr1)

# arr1 = []
# n = 5
# for i in range(1, n+1):
#     for j in range(i):
#         arr1.append(i)
#         print(arr1)


# s = 'qwertyuiopasdfghjklzxcvbnm'
# lst = []
# for i, j in enumerate(s):
#     lst.append(j * (i + 1))
# for item in lst:
#     print( *item)


# i = 5
# while i < 25:
#     print(i)
#     i = i + 2


# c = (1,2,3)
# print(c[0])

# a = (1)
# print(type(a))

c = (1,[1,2,3],6,9,4,5,[0,0,0])
# c[1] = [2,3,4] #Ошибка
# c[1].append(4) #Изменяет все таки кортеж :) Т.к. кортеж хранит ссылки, а не сами элементы. Ссылки то и не изменяются!
c[1].pop()
c[3].pop() # такое работает только с элементом массива кортежа
print(c)