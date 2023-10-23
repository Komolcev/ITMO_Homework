# 16-1:
import re
dct = {1: 1, 2: 2, 3: {2: 22, 3: {1: 111, 2: 222,
                                  3: {0: 1111, 1: 2222, 2: 3333}}, 1: 11, }, 6: 22}
x = int(input('Введите ключ к dct: '))


def get_values(dct, x):
    values = []
    for key, value in dct.items():
        if key == x:
            values.append(value)
        elif isinstance(value, dict):
            values.extend(get_values(value, x))
    return values


result = get_values(dct, x)
print(result)


# 16-2:


def print_car_numbers(text):
    text = text.upper()
    pattern = re.compile(
        r'[A-ZА-Я]{1}[0-9]{3}[A-ZА-Я]{2}[178]{3}|[A-ZА-Я]{1}[0-9]{3}[A-ZА-Я]{2}[78]{2}')
    matches = re.findall(pattern, text)
    for match in matches:
        print(match)


text = input('Введите номера автомобилей через запятую: ')
print_car_numbers(text)


# 16-3:


def find_phone_numbers(text):
    pattern = r'(\+7\((812|921)\)\d{3}-\d{2}-\d{2}|\+7\((812|921)\)\d{3}-\d{4})'
    phone_numbers = re.findall(pattern, text)
    correct = []
    for num in phone_numbers:
        correct.append(num[0])
    return correct


text = "+7(812)123-45-67, +7(921)987-65-43, +7(812)111-2233, +7(911)555-6677"
phone_numbers = find_phone_numbers(text)
for numb in phone_numbers:
    print(numb)
