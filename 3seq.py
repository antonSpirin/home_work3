count_list_first = int(input('Введите количество элементов в первом списке - '))
list_first = []

for i in range(count_list_first):
    list_first.insert(i, input(f'Введите {i + 1} элемент списка '))

print('Первый список: ', list_first)

count_list_second = int(input('Введите количество элементов во втором списке - '))
list_second = []

for i in range(count_list_second):
    list_second.insert(i, input(f'Введите {i + 1} элемент списка '))

print('Второй список: ', list_second)

for element in list_second:

    if int(element in list_first) == 1:  # проверка на вхождение элементов второго списка в первый
        list_first.remove(element)

print('Итоговый список после проверки: ', list_first)
