# print('Hello world!')

# 1*2*3*4*5….
# 100/5 = 20 …
# 25 50 75 100 - еще по 4-ке
# Итого в 100! = 24 нолика
# 1000?? 24 умножить на 4

# Михаил Зимнев
# Программирование - алгоритмы и структуры данных
# Сериал Монти Пайтон

# https://docs.python.org/3/
# Линус Торальдс
# Python autumn work 2023
# m.zimnev@yandex.ru
# Отправить репозиторий на почту


# Программа 1
# s = input('Как тебя зовут? ')
# print(f'Привет, {s}!')
# old = int(input('How old are you? '))
# print(f'Мне {old * 2} лет')

# old = 'asdasdasdsa'

# # Хулиганство (он s присвоил функцию принт)
# s = print
# s('ddddd')

# Программа 2
a = input('Ваше имя? ')
b = input('Ваше фамилия? ')
c = input('Ваше отчество? ')

# print(c, b, a, sep=':')
# print(f'Привет, {b} {c} {a}')
# print(f'Привет, {}')

print(' '.join([c, b, a]), sep=':')
print(' '.join([c, b, a])[::-1])
print(f'{c+b}:{a}')

# command+option+l = делает все по pip8
# command + '?/' = #
# Динамическая типизация + или - ?

# import keyword
# print(*keyword.kwlist)
# # * убирает все лишнее

x = float(input('Введите цифру: '))
if x > 0:
    print('Положительное!')
elif x < 0:
    print('Отрицательное!')
else:
    print('Равно 0!')
