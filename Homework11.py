# # 11-1:
# import calendar

# def free_dates(year):
#     free_days = []
#     for month in range(1, 13):
#         first_day_of_month = calendar.weekday(year, month, 1)
#         if first_day_of_month == 3:
#             third_thursday = 15
#         elif first_day_of_month < 3:
#             third_thursday = 15 + (3 - first_day_of_month)
#         else:
#             third_thursday = 15 + (10 - first_day_of_month)
#         free_days.append((year, month, third_thursday))
#     return free_days

# free_museum_days_2023 = free_dates(2023)

# for year, month, day in free_museum_days_2023:
#     print(f"{day:02d}-{month:02d}-{year}")


# 11-2:
# spisok = []
# with open('task1.txt') as f:
#     for spi in f:
#         spisok.append(spi.split(','))
# import openpyxl
# wb = openpyxl.Workbook()
# ws = wb.active
# spsk = sorted(spisok, key = lambda x: (x[3], x[1], x[2]))
# Itogo = 0
# for spi in spsk:
#     ws.append(spi)
#     Itogo += float(spi[-1])
# ws.append(['Итого: ', Itogo])
# wb.save('task1.xlsx')


# # 11-3:
# def arabic_to_roman(number):
#     if not 1 <= number <= 3999:
#         return "Неверное число"

#     num = {
#         1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
#         10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
#         100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
#         1000: 'M'
#     }

#     roman_number = ''
#     for value in sorted(num.keys(), reverse=True):
#         while number >= value:
#             roman_number += num[value]
#             number -= value
#     return roman_number


# arabic_number = int(input())
# roman_number = arabic_to_roman(arabic_number)
# print(f"Арабское число {arabic_number} в римской нотации: {roman_number}")
