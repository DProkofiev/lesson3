# -- методы списков: --
# list.append(x), list.index(x, [start [, end]]), list.sort([key=функция]), list.remove(x), list.count(x)

# -- методы словарей: --
# dict.items(), dict.popitem(), dict.update([other]), dict.values(), dict.get(key[, default])

# -- методы множеств: --
# set.union(other, ...), set.intersection(other, ...), set.difference(other, ...), set.add(elem), set.remove(elem)

# -- методы строк:--
# S.find(str, [start],[end]), S.split(символ), S.lower(), S.format(*args, **kwargs), S.strip([chars])


# Задание 1
# Пользователь вводит количество элементов будущего списка
# После этого по очереди по одной вводит любые цифры
# Сохранить цифры в список
# Отсортировать список по возрастанию и вывести на экран

digits_list = []
input_error = 'введено не целое число. Повторите ввод'
print('введите количество элементов в вашем списке')
while True:
    count_items = input()
    if count_items.isdigit():
        count_items = int(count_items)
        break
    else:
        print(input_error)
for i in range(0, count_items):
    print('введите',i,'элемент списка')
    while True:
        digit = input()
        if digit.isdigit():
            digits_list.append(int(digit))
            break
        else:
            print(input_error)
digits_list.sort()
print(digits_list)