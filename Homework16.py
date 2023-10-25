# 16-1:
import re


def create_abbreviation(string):
    abbreviation = ''.join(re.findall(r'\b[A-Z]', string))
    return abbreviation


abbreviation = create_abbreviation(input(str('Введите строку: ')))
print(abbreviation)


# 16-2:
arr1 = [-10, -1, 0, 1, 10, 5, 90, 20, 45, -17, 60, 30, 3, 75, 100]
num = int(input('Введите положительное целое число: '))


def find_numbers(num, arr):
    array_str = ' '.join(map(str, arr))
    result = re.sub(r'-\d+', '', array_str)

    pattern = r'\b(?:0|[1-9]\d{0,1})\b'
    matches = re.findall(pattern, result)

    filtered_numbers = []
    for match in matches:
        if int(match) < num:
            filtered_numbers.append(match)

    return filtered_numbers


numbers = ' '.join(find_numbers(num, arr1))
print(numbers)


# 16-3:
def to_lowercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.lower()
        return result
    return wrapper


@to_lowercase
def say():
    str = input('Напишите что-то сюда: ')
    return str


print(say())
