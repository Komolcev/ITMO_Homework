# 16-1:
import re


def generate_acronym(text):
    words = re.findall(r'\b\w', text)
    acronym = ''.join(words).upper()
    return acronym


sentence = input(str('Введите строку: '))

acronym = generate_acronym(sentence)
print(acronym)


# 16-2:


def find_positive_numbers(num, arr):
    pattern = r'\b(?:[0-9]|[1-{}][0-9])\b(?![0-9])'.format(num, num)
    matches = re.findall(pattern, ' '.join(map(str, arr)))
    return list(map(int, matches))


num = int(input('Введите положительное целое число: '))
arr1 = [0, 1, 5, 10, 15, 99, 20, 25, 30, 45, 60, 1, 70, 80, 100]
result = find_positive_numbers(num, arr1)
result = [x for x in result if x != num]
print(' '.join(map(str, result)))


# # 16-3:
# def to_lowercase(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if isinstance(result, str):
#             return result.lower()
#         return result
#     return wrapper


# @to_lowercase
# def say():
#     str = input('Напишите что-то сюда: ')
#     return str


# print(say())
