# 7-1:
def find_lcm(*args):
    # Функция для вычисления НОД
    def find_gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    # Функция для вычисления НОК
    def find_lcm_two_numbers(x, y):
        return (x * y) // find_gcd(x, y)

    # Инициализируем НОК первых двух чисел
    lcm = args[0]

    # Вычисляем НОК для остальных чисел по очереди
    for i in range(1, len(args)):
        lcm = find_lcm_two_numbers(lcm, args[i])

    return lcm


# Запрашиваем числа у пользователя
numbers = input("Введите числа через пробел: ").split()

# Преобразуем строки в целые числа
numbers = [int(num) for num in numbers]

# Вызываем функцию find_lcm, передавая в нее список чисел в качестве аргументов
lcm_result = find_lcm(*numbers)

# Выводим результат
print("Наименьшее общее кратное (НОК):", lcm_result)





# 7-2:
arr1 = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
        'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
arr2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
        'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}


def code(string, n):
    new_str = []
    for i in string:
        if i in arr1:
            shifted_value = (arr1[i] + n - 1) % 26
            new_char = chr(shifted_value + ord('A'))
            new_str.append(new_char)
        elif i in arr2:
            shifted_value = (arr2[i] + n - 1) % 26
            new_char = chr(shifted_value + ord('a'))
            new_str.append(new_char)
        else:
            new_str.append(i)
    return new_str


string = input('Введите предложение: ')
n = int(input('Введите число, на которое будет сдвинуты буквы: '))
print(''.join(map(str, code(string, n))))







# 7-3:
def max3(x):
    # Преобразуем двумерный список в одномерный
    flattened = [num for sublist in x for num in sublist]
    sorted_nums = sorted(set(flattened), reverse=True)  # Сортируем числа
    return sorted_nums[:3]  # Возвращаем первые три самых больших числа


n = int(input())
m = int(input())
x = []
for i in range(n):
    x.append([])
    for j in range(m):
        x[i].extend(input())

result = max3(x)
print(*result[::-1])
