# Пользователь вводит любые цифры через запятую
# Сохранить цифры в список
# Получить новый список в котором будут только уникальные элементы исходного (уникальным считается символ, который встречается в исходном списке только 1 раз)
# Вывести новый список на экран
# Порядок цифр в новом списке не важен
digits_list = []
print('введите список целых чисел через разделитель "," ";" или "/"')
digits_str = input()
if len(digits_str.split('/')) != 1:
    digits_list = digits_str.split('/')
if len(digits_str.split(';')) != 1:
    digits_list = digits_str.split(';')
if len(digits_str.split(',')) != 1:
    digits_list = digits_str.split(',')
digits_list = [int(item) for item in digits_list]
digits_list.sort()
digits_unique_list = []
for item in digits_list:
   if digits_list.count(item) == 1:
      digits_unique_list.append(item)
print('исходный список ',digits_list)
print('уникальный список ',digits_unique_list)