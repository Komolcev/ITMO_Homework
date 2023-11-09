# 9-1:
arr1 = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'T'}


def changed(string):
    def split(string):
        return [char for char in string]

    split_string = split(string)
    changed_string = [arr1[char] for char in split_string]
    result = ''.join(changed_string)
    return result


string = str(input('Введите ДНК: '))
print(changed(string))


# 9-2:
arr1 = ['а', 'у', 'о', 'ы', 'и', 'э', 'ю', 'я', 'ё', 'е',
        'А', 'У', 'О', 'Ы', 'И', 'Э', 'Ю', 'Я', 'Ё', 'Е']
arr2 = []


def similar(x, n, arr2):
    vowel_positions_x = [i for i, char in enumerate(x) if char in arr1]
    matching_words = []
    for word in arr2:
        vowel_positions_word = [
            i for i, char in enumerate(word) if char in arr1]
        if vowel_positions_x == vowel_positions_word:
            matching_words.append(word)
    return matching_words


x = str(input('Введите слово для сравнения: '))
n = int(input('Сколько будет слов для проверки: '))
for i in range(n):
    word = input('Введите слово: ')
    arr2.append(word)

print(similar(x, n, arr2))


# 9-3:
def how_many(text):
    # привести текст к нижнему регистру
    text = text.lower()
    # создать словарь для подсчета символов и их частоты
    dictionary = {}
    # разбить текст на символы
    for char in text:
        # обновить словарь
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    # отсортировать словарь по частоте встречаемости символов
    sorted_dict = sorted(dictionary.items(), key=lambda x: (-x[1], x[0]))
    # вывести первые 10 наиболее часто встречающихся символов
    for i in range(min(10, len(sorted_dict))):
        print(sorted_dict[i][0], ":", sorted_dict[i][1])


text = str(input('Введите текст: '))
print()
how_many(text)
