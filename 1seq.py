# Формируем список
count_list = int(input('Введите количество элементов в списке - '))
new_list = []

for i in range(count_list):
    new_list.insert(i, input(f'Введите {i + 1} элемент списка '))

print('Первоначальный список: ', new_list)
new_list.sort()
print('Список отсортированный по возрастанию: ', new_list)

