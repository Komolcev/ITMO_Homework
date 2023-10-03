# 7-1:
# НОК = (A * B) / НОД
a, b = map(int, input('Введите 2 числа через пробел: ').split())
x = a * b
# Нахоdим НОД (наибольший общий делитель):
while b > 0:
    a = b
    b = a % b
# Находим НОК:
print(int(x / a))


# 7-2:
arr1 = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
        'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
arr2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
        'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}


def code(string, n):
    new_str = []
    for i in string:
        if i in arr1:
            new_str.append(arr1[i]+n)
        elif i in arr2:
            new_str.append(arr2[i]+n)
        else:
            new_str.append(i)
    return new_str


string = input('Введите предложение: ')
n = int(input('Введите число, на которое будет сдвинуты буквы: '))
print(''.join(map(str, code(string, n))))


# 7-3:
# Кривой, косой, зато свой код!
# Долго не мог понять как числа попадают в двумерный массив на вход. Потом решил все же сделать так,
# Что пользователь сам вводит числа и они уже разбиваются на вложенные подмассивы.
def maximum_number(numbers):
    arr1 = []
    maximum = 0
    maximum_position = 0
    arr2 = []
    split_numbers = numbers.split()
    for num in split_numbers:
        arr1.append(list(map(int, num)))

    for _ in range(3):
        for i in range(len(arr1)):
            sublist = arr1[i]
            temp_max = max(sublist)
            if temp_max > maximum:
                maximum = temp_max
                maximum_position = i

        arr2.append(maximum)
        arr1[maximum_position].remove(maximum)

        maximum = 0
        maximum_position = 0

    return arr2


numbers = input("Введите числа через пробел: ")
print(maximum_number(numbers))
