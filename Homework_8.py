# 8-1:
def genetics(arr1):
    i = 0
    while i < len(arr1) - 1:
        tek = arr1[i]
        sled = arr1[i+1]
        if (tek == "А" and sled == "Г") or (tek == "Г" and sled == "А"):
            arr1[i] = sled
            arr1[i+1] = tek
            i = i + 1
        if (tek == "Ц" and sled == "Т") or (tek == "Т" and sled == "Ц"):
            arr1.insert(i+1, "А")
            arr1.insert(i+2, "Г")
            i = i + 2
        i = i + 1
    return arr1


string = input("Введите строку кода заглавными русскими буквами: ")
arr1 = list(string)
print(''.join(genetics(arr1)))


# 8-2:
list = [[1, 5, 3], [2, 44, 66, 1, 4], [53333, 5], [7, 9, 8, 9]]
# Функция для вычисления общего количества цифр в подсписке


def count_digits(sublist):
    return sum(map(lambda x: len(str(x)), sublist))


# Сортировка каждого подсписка по убыванию
sorted_sublists = [sorted(sublist, reverse=True) for sublist in list]
# Сортировка внешнего списка по возрастанию общего количества цифр в каждом подсписке
sorted_list = sorted(sorted_sublists, key=count_digits)
print(sorted_list)


# 8-3:
lst = ['abab', 'xx', 'aaaaaaa', 'abcbab']
lst2 = sorted(lst, key=lambda x: (-len(set(x)), x))
print(lst2)
