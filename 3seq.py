#Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
#Затем он вводит элементы 2-го списка
#Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
digits_list_1 = []
digits_list_2 = []
print('введите первый список целых чисел через разделитель "," ";" или "/"')
digits_str_1 = input()
if len(digits_str_1.split('/')) != 1:
    digits_list_1 = digits_str_1.split('/')
if len(digits_str_1.split(';')) != 1:
    digits_list_1 = digits_str_1.split(';')
if len(digits_str_1.split(',')) != 1:
    digits_list_1 = digits_str_1.split(',')
digits_list_1 = [int(item) for item in digits_list_1]
digits_list_1.sort()
print('введите второй список целых чисел через разделитель "," ";" или "/"')
digits_str_2 = input()
if len(digits_str_2.split('/')) != 1:
    digits_list_2 = digits_str_2.split('/')
if len(digits_str_2.split(';')) != 1:
    digits_list_2 = digits_str_2.split(';')
if len(digits_str_2.split(',')) != 1:
    digits_list_2 = digits_str_2.split(',')
digits_list_2 = [int(item) for item in digits_list_2]
digits_list_2.sort()
print('первый список:', digits_list_1)
print('второй список:', digits_list_2)
for i in digits_list_1:
    for j in digits_list_2:
        if j in digits_list_1:
            digits_list_1.remove(j)
print('первый список - второй список =',digits_list_1)
