# 15-1:
import re
dct = {1: 1, 2: 2, 3: {2: 22, 3: {1: 111, 2: 222,
                                  3: {0: 1111, 1: 2222, 2: 3333}}, 1: 11, }, 6: 22}
x = int(input('Ключ: '))


def dct_val(dct, x):
    r = []
    for k, v in dct.items():
        if k == x:
            r.append(v)
        if type(v) == dict:
            s = dct_val(v, x)
            r.extend(s)
    return r


print(*dct_val(dct, x), sep='\n')


# # 15-2:
# import re
# def print_car_numbers(text):
#     text = text.upper()
#     pattern = re.compile(r'[АОМТВНЕРХСУКAOMTBHEPXCYK]{1}[0-9]{3}[АОМТВНЕРХСУКAOMTBHEPXCYK]{2}[178]{3}|[АОМТВНЕРХСУКAOMTBHEPXCYK]{1}[0-9]{3}[АОМТВНЕРХСУКAOMTBHEPXCYK]{2}[78]{2}')
#     matches = re.findall(pattern, text)
#     for match in matches:
#         print(match)
# text = input('Введите номера автомобилей через запятую: ')
# print_car_numbers(text)


# # 15-3:
# def find_phone_numbers(text):
#     pattern = r'(\+7\((812|921)\)\d{3}-\d{2}-\d{2}|\+7\((812|921)\)\d{3}-\d{4})'
#     phone_numbers = re.findall(pattern, text)
#     correct = []
#     for num in phone_numbers:
#         correct.append(num[0])
#     return correct
# text = "+7(812)123-45-67, +7(921)987-65-43, +7(812)111-2233, +7(911)555-6677"
# phone_numbers = find_phone_numbers(text)
# for numb in phone_numbers:
#     print(numb)
