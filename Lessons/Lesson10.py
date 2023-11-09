# Эксель
# # 0 в конце это то, как заполнить значение словаря - нулем
# # 3 значения выдает потому, что всего три разных числа лежат в массиве: -1,0,1
# dct = dict.fromkeys([0,-1,1,0,-1,-1,0,-1,1], 0)
# print(len(dct))
# print(sorted(dct, key = lambda x: -abs(x)))


# tcid = {1:{1:{1:{1:111111}}}}
# print(tcid[1][1][1][1])


# # Тут обращается к 111111
# tcid = {1:{2:{3:{4:111111}}}}
# print(tcid[1][2][3][4])


# # Counter делает автоматически
# import collections
# s = input()
# d = collections.Counter(s)
# # Большая буква = класс
# for k,v in d.items():
#     print(k, v)


# import collections
# d = collections.Counter(['a','a',2,3,3,6])
# for k,v in d.items():
#     print(k, v)


# # Список
# import collections
# d = collections.Counter(('a','a',2,3,3,6))
# for k,v in d.items():
#     print(k, v)


# import collections
# dir(collections)


# import collections
# a = collections.Counter('aabbbcccccddddddd432')
# print(dict(a))
# # Counter удобная вещь чтобы все считать


# a = {1:11}
# print(type(a))


# dct = {0:0, 1:{11:{111:1111}}, 2:{22:{222:2222}}, 3:{33:333}, 4:444}
# for k, v in dct.items():
#     print(k, v)
#     if type(v) == dict:
#         for a, b in v.items():
#             print('   ',a,b)
#             if type(b) == dct:
#                 for x, y in m.items():
#                     print('      ', x,y)


# # Открыть другой файл
# f = open('Lyrics.txt', encoding = 'utf-8')
# s = f.read()
# for i in s:
#     print(i, end='')
# f.close()


# # Открыть только 140 символов
# f = open('Lyrics.txt', encoding = 'utf-8')
# s = f.read(140)
# for i in s:
#     print(i, end='')
# f.close()


# # оператор read понимает где мы остановились
# f = open('Lyrics.txt', encoding = 'utf-8')
# s = f.read(20)
# p = f.read(20)
# print(s, p, sep = '')
# f.close()


# f = open('Lyrics.txt', encoding = 'utf-8')
# for i in range(5):
#     s = f.read(10)
#     # print('\n' + s)
#     print(s.strip())
# f.close()


# f = open('Lyrics.txt', encoding = 'utf-8')
# s = f.readlines()
# # print(type(s))
# print(s)
# # for i in s:
# #     print(i.strip())
# f.close()


# f = open('Lyrics.txt', encoding = 'utf-8')
# s = f.readlines()
# print(s[-1])
# f.close()


# f = open('Lyrics.txt', encoding = 'utf-8')
# lst = f.readlines()
# for i, j in enumerate(lst):
#     print(i, j.strip())
# f.close()


# f = open('Lyrics.txt', encoding = 'utf-8')
# lst = f.readlines()
# for i, j in enumerate(lst):
#     print(i, j.strip('/n'))
# f.close()


# f = open('Lyrics.txt', encoding = 'utf-8')
# lst = f.readlines()
# for i, j in enumerate(lst, 123):
#     print(i + 1, j.strip('/n'))
# f.close()


# f = open('Lyrics.txt', encoding = 'utf-8')
# s = f.readline()
# print(s.strip())
# s = f.readline()
# print(s.strip())
# f.close()


# f = open('Lyrics.txt', encoding = 'utf-8')
# s = f.readline()
# # print(s.strip()) # Только вторую строчку распечатает
# s = f.readline()
# print(s.strip())
# f.close()


# f = open('Lyrics.txt', encoding = 'utf-8')
# for i in range (1,5):
#     s = f.readline()
#     print(i, s.strip())
# f.close()


# f = open('Lyrics.txt', encoding = 'utf-8')
# print(f)
# for i in f:
#     print(i.strip())
# f.close()


# !!!!!Перезапись! 'w' - удаляет вообще всё!!!!!
# f = open('Lyrics.txt', mode = 'w', encoding = 'utf-8')
# f.write('The first line\n')
# f.write('The second line\n')
# f.write('The third line')
# f.close()


# f = open('Lyrics.txt', mode = 'r', encoding = 'utf-8')
# for i in f:
#     print(i)
# f.close()


# f = open('Lyrics.txt', mode = 'w', encoding = 'utf-8')
# f.write('The first line\n')
# f.write('The second line\n')
# f.write('The third line\n')
# a = ['Первый элеменнт списка\n','Второй элеменнт списка\n']
# f.writelines(a)
# f.close()


# mode = 'r' - реад, чтение
# f = open('Lyrics.txt', mode = 'r', encoding = 'utf-8')
# s = f.read()
# print(s)
# f.close()

# mode = 'w' - врайт, писать
# g = open('Lyrics.txt', mode = 'w', encoding = 'utf-8')
# g.write(s)
# g.close()


# readlines() - читает строки (когда нам что то надо найти)
# f = open('Lyrics.txt', mode='r', encoding='utf-8')
# s = f.readlines() # содержимое файла попало в список
# print(s)
# f.close()

# ищем цифры в Lyrics.txt
# g = open('Lyrics.txt', mode = 'w', encoding='utf-8')
# for i in s:
#     for j in i:
#         if j.isdigit():
#             g.write(i)
#             break
# g.close()


# openpyxl
# Это пакет, модуль. Это можно точно так же удалить, если не надо.
# Посмотреть все модули можно командой
# help("modules") # - все установленные модули на компьютере


# # Создаем файл расширением xlsx (создание книги Excel (workbook))
# import openpyxl
# from openpyxl import Workbook
# wb = Workbook() # Это экземпляр класса Workbook
# wb.save('test.xlsx') # Сразу записываем его пустым


# Таблицы:
# import openpyxl
# wb = openpyxl.load_workbook('test.xlsx')  # Открываем книгу существующую
# print(wb.sheetnames)  # Список листов

# ws = wb.active  # Это активный рабочий лист
# print(ws.title)

# # Запись
# ws['A1'].value = 'Иванов'
# ws['B1'].value = '123'
# ws['A2'].value = 'Петров'
# ws['B2'].value = '234'
# ws['A3'].value = 'Сидоров'
# ws['B3'].value = '345'
# wb.save('test.xlsx')

# wb.create_sheet('List1')  # Создаем лист новый
# ws3 = wb['List1']  # Создаем другой лист
# print(ws3.title)  # Посмотрим

# print(wb.sheetnames)  # Список листов
# wb.active = wb['List1'] # Назначение другого рабочего стола
# wb.remove(ws) # Удаление рабочего стола
# wb.save('test.xlsx')

# # Он тут создавал, добавлял и удалял листы
# # Доступ к ячейкам

# s = ws3['A1'].value
# print(s)

# # Изменение ячейки (перезаись)
# ws3['A1'].value = 123
# p = ws3['A1'].value
# print(p)

# wb.save('test.xlsx')
# Работать с файлом который не закрыт программа не разрешает

# print(ws3.cell(row=1, column=1,).value)

# Распечатать номер ряда и номер колонки. Мы можем работать со страницей, как с двумерной матрицей

# i, j = 1, 1
# for i in range (1, 3):
#     print(i, ws3.cell(row = i, column = 1).value)
# print(ws3.cell(row=i, column=j).value)
# print(ws3.cell(row=i, column=j + 1).value)
# wb.save('test.xlsx')
