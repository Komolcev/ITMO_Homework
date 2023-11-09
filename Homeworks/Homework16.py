# # 16-1:
# import re
# def generate_acronym(text):
#     words = re.findall(r'\b\w', text)
#     acronym = ''.join(words).upper()
#     return acronym
# sentence = input(str('Введите строку: '))
# acronym = generate_acronym(sentence)
# print(acronym)


# ДЗ 16-2:
import re
n = int(input('--->'))
x, y = divmod(n, 10)  # * Замена // и %
r = []
r.append(r'\b\d\b')  # от 0 до 9
r.append(r'\b10\b')  # 10
if n == 10:
    regex = '|'.join(r[:2])
elif n < 20:
    r.append(rf'\b1[0-{y}]\b')  # от 10 до 19
    regex = '|'.join(r[:3])
else:
    r.append(rf'\b[1-{x-1}]\d\b')  # от 10 до 39
    # от 40 до 45, а если написать {y-1}, тогда будет не включая
    r.append(rf'\b{x}[0-{y}]\b')
    regex = '|'.join(r[:4])
print(*re.findall(regex, str(list(range(200)))))


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
