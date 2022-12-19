str_list = input('Введите любые цифры черз запятую: ')
first_list = str_list.split(',')
print('Исходный список: ', first_list)
new_list = []  # список уникальных значений первого списка

for digit in first_list:
    if int(first_list.count(digit)) == 1:  # проверка элементов списка н уникальность
        new_list.append(digit)

print('Новый список с уникальными значениями из первого списка: ', new_list)
