# # Нельзя менять список в процессе выполнения программы!
# lst = [1,2,3,4,5]
# for x in lst:
#     a = lst.pop()
#     print(x,a, lst)
# print(lst)


# lst = [1,2,3,4,5]
# for x in lst:
#     a = lst.pop(0)
#     print(x, a, lst)
# print(lst)


# # ДЗ-1
# def signs():
#     i = 0
#     s = -1
#     while True:
#         i = i + 1
#         s = -s
#         yield i * s
# gen = signs()
# for i in range(int(input('Введите номер '))):
#     print(next(gen), end = ',')


# def divide(x, y):
#     try:
#         out = x/y
#     except:
#         try:
#             important math
#             out = math.inf* x / abs(x)
#         except:
#             out = None
#     finally: # Try, exept and finally
#         return out
# print(divide(0,0))


# # Исключения
# def validate (name):
#     if len(name) < 10:
#         raise ValueError
# try:
#     name = input('--->')
#     validate(name)
# except ValueError:
#     print('Короткое')
# else:
#     print('OK!')


# class NameTooShortError(ValueError):
#     pass
# def validate(name):
#     if len(name) < 10:
#         raise NameTooShortError


# class Positive (ValueError):
#     pass
# class Negative (ValueError):
#     pass
# def f(lst):
#     for i in lst:
#         try:
#             if i > 0: raise Positive
#             elif i < 0: raise Negative
#         except Positive:
#             print('Положительное')
#         except Negative:
#             print('Отрицательное')
#         else:
#             print('0')
#     return
# f([1,2,0,11,-22,0])


# def rep(v, mr):
#     c = 0
#     while True:
#         if c >= mr:
#             return
#         c += 1
#         yield v, c
# for x in rep('OK', 5):
#     print(x)


# def rep123():
#     yield 1
#     yield 2
#     yield 3
# # print(*rep123())
# # print(4 in rep123())
# # n1, n2, n3 = rep123()
# # print(n1,n2,n3)
# gen = rep123()
# print(2 in gen)
# print(next(gen))
# print(next(rep123()))
# print(next(gen))
# gen = rep123()
# print(len(gen))


# # Тут генератор создается дважды!
# def fg1():
#     yield 'Red'
#     yield 'Green'
#     yield 'Blue'


# def fg2():
#     yield 'Round'
#     yield from fg1()
#     yield 'Square'
#     yield from fg1()
#     yield "Rectangle"
# print(*fg2())


# lc = (i for i in range(10))
# for i in lc:
#     print(i)


# def inte(n):
#     for i in range(n): yield i
# def evens(iterable):
#     for i in iterable:
#         if i % 2 == 0: yield i
# def sq(iterable):
#     for i in iterable: yield i * i
# chain = sq(evens(inte(10)))
# print(*chain)


# def numb(a = 65, z = 91):
#     yield from range(a, z)

# def rhc(iterable):
#     for i in iterable:
#         yield chr(i)
# chain = rhc(numb(a = 97, z = 97 + 26))
# print(*chain)


# # Рекурсия
# # Путешествие хоббита туда и обратно
# # Раскладывается от 3х до нуля и потом обратно от нуля до 3х
# def funct(n):
#     print(111, 'funct', n)
#     n -= 1
#     if n > 0:
#         funct(n)
#     print(222, 'cnuf', n)
#     return
# funct(3)


# def fact(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(1))


def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)


print(sum(5))
