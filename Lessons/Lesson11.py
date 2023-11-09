# # Разминка:
# import calendar
# import locale
# from datetime import *
# f = open('test.txt', 'w')
# f.write('1234567890')
# f.close()

# g = open('test.txt')
# print(1, len(g.read(4)))  # Прочитать только 4 символа, вывести длину
# print(2, len(g.read()))  # Вывести длину

# 10-1:
# import openpyxl
# # Заполняем лист эксель самостоятельно
# wb = openpyxl.load_workbook('test.xlsx')
# ws = wb['Лист1']
# print(ws.title)

# d = {}
# for i in range(i, ws.max_row + 1):
#     fio = ws.cell(i, 1).value
#     print(fio)
#     sal = ws.cell(i, 2).value
#     d[fio] = d.get(fio, 0) + sal
# print(d)

# ws = wb['Лист2']
# for i, fio in enumerate(d.keys()):
#     ws.cell(i, + 1, 1).value = fio
#     ws.cell(i, + 1, 2).value = d[fio]
# mr = ws.max_row + 1
# ws.cell(mr, 1).value = 'ИТОГО: '
# ws.cell(mr, 2).value = sum(d.values())
# wb.save('test.xlsx')


# Работа с файлами txt:
# f = open('test.txt')
# s = f.read()
# print(s)
# f.close()
# g = open('test.txt')
# # g.write(s[::2]) # Тут можно записать каждый второй символ в другой документ (+ исправить выше)
# print(s[::2])
# g.close()

# # Задание: прочитать строки текста из одного файла в другой, отсортировать внутри строки слова по возрастанию
# # и записать обновленные строки в другой файл
# # Из одного файла скопировали текст в другой:
# f = open('test.txt', 'r')
# s = f.readlines()
# f.close()

# # Разбить по словам, привести к нижнему регистру, отсортировать по алфавиту
# g = open('test1.txt', 'w')
# for i in s:
#     j = sorted(i.split(), key=lambda x: x.lower())
#     # g.write(' '.join(j) + '\n')
#     print(' '.join(j) + '\n', file = g) # Перенос строки автоматически добавляется
# g.close


# # Менеджер контекста:
# with open('test.txt', 'r') as f:
#     s = f.readlines()
# # f.close() можно не писать

# with open('test1.txt', 'a') as g:
#     for i in s:
#         j = sorted(i.split(), key=lambda x: x.lower())
#     print(' '.join(j) + '\n', file = g) # Перенос строки автоматически добавляется


# # Опять поработаем с эксель (Надо создать эксель)
# import openpyxl
# wb = openpyxl.load_workbook('test1.xlsx')
# ws = wb['New']
# for i in range(ws.max_row):
#     for j in range(ws.max_column):
#         print(ws.cell(row = i + 1, column = j + 1).value, end = ' ')
#     print()


# import time
# print(time.time()) # время с 70-го года (сек)
# print(time.ctime()) # Текущее время !
# # Засечь время
# t0 = time.time()
# su = 0
# for i in range(100000):
#     su += 2 ** i
# t1 = time.time()
# print(t1-t0)


# # +5 секунд
# import time
# t0=time.time()
# print(t0)
# t0 = time.time()
# print(time.ctime(t0))
# time.sleep(5)
# print(time.ctime())

# print(dir(time))
# perf_counter для более четкой проверки времени работы кода

# # Текущая дата
# import datetime
# print(datetime.datetime.today())


# # Работа с date time
# from datetime import *
# print(date(2023, 10, 11))

# from datetime import *
# print(time(21, 52, 0))

# # Время не зависит от даты
# from datetime import *
# print(datetime(2023,10,11,20,53,0))
# a = datetime(2023,12,31,23,59,59)
# print(a)
# b = timedelta(0,1) # Приращение времени
# print(b)
# c = a + b
# print(type(c))


# from datetime import *
# a = date(2023,12,31)
# print(a)
# b = timedelta(days = 1) # Приращение времени
# c = a + b
# print(c)


# * - значит всё импортировать
# from datetime import *
# a = date(2023,12,31)
# print(a)
# b = timedelta(days = 1) # Приращение времени
# c = a + b
# print(c)


# from datetime import *
# a = date(2023,12,31)
# print(a.year, a.month)


# b = datetime.today()
# print(b.hour, b.minute)

# # Преобразование в формат
# print(datetime.strptime('10/11/2023', '%m/%d/%y')) # % - маска

# b = datetime.today()
# print(b.strftime('%d   %m.%y'))
# print(b.strftime('%D----%M/%Y'))

# b = datetime.now()
# print(b)

# b = datetime(2017,11,28,23,59,50)
# print(b.strftime('%A %D %B %Y'))


# # Текущее время
# from datetime import datetime
# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
# current_date = datetime.now()
# print(current_date.strftime('%A %d %B %Y'))


# # Пример РУ и ФР и США
# import locale
# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
# b = datetime(2023, 11, 30)
# print(b.strftime('%A %d %B %Y'))

# locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
# b = datetime(2023, 11, 28)
# print(b.strftime('%A %d %B %Y'))

# locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
# b = datetime(1995, 12, 1)
# print(b.strftime('%A %d %B %Y'))

# print(calendar.weekday(2023, 10, 11))
# # ПН = 0
# print(calendar.monthcalendar(2023, 10))
# # Целый календарь
# print(calendar.month(2023, 10))
# # isleap - високосный год

# Посчитать сколько пн, вт и тд в году:
# import calendar, datetime
# year = int(input('Введите год: '))
# b = datetime.date(year, 12, 31)
# print(b, calendar.weekday(b.year, b.month, b.day))
