import random

dict_celeb = {'А.С. Пушкин': '06.06.1979', 'Л.Н.Толстой': '09.09.1828', 'Ф.М.Достоевский': '11.11.1821',
              'А.П.Чехов': '29.01.1960', 'И.С.Тургенев': '09.11.1918', 'А.И.Солженицын': '11.12.1918',
              'А.А. Фет': '05.12.2020', 'М.Ю. Лермонтов': '15.10.1984', 'C.А. Есенин': '03.10.1985',
              'Ф.И. Тютчев': '05.12.1983'}

list_name_keys = list(dict_celeb.keys())
print(list_name_keys)
count_names = 5
select_names = random.sample(list_name_keys, count_names)
print(select_names)

date_dict = {'01': 'Первое', '02': 'Второе', '03': 'Третье', '04': 'Четвёртое', '05': 'Пятое', '06': 'Шестое',
             '07': 'Седьмое',
             '08': 'Восьмое', '09': 'Девятое', '10': 'Десятое', '11': 'Одиннадцатое', '12': 'Двенадцатое',
             '13': 'Тринадцатое',
             '14': 'Четырнадцатое', '15': 'Пятнадцатое', '16': 'Шестнадцатое', '17': 'Семнадцатое',
             '18': 'Восемнадцатое',
             '19': 'Девятнадцатое', '20': 'Двадцатое', '21': 'Двадцать первое', '22': 'Двадцать второе',
             '23': 'Двадцать третье', '24': 'Двадцать четвертое', '25': 'Двадцать пятое', '26': 'Двадцать шестое',
             '27': 'Двадцать седьмое', '28': 'Двадцать восьмое', '29': 'Двадцать девятое', '30': 'Тридцатое',
             '31': 'Тридцать первое'}
list_date_keys = list(date_dict.keys())

month_dict = {'01': 'Января', '02': 'Февраля', '03': 'Марта', '04': 'Апреля', '05': 'Мая', '06': 'Июня', '07': 'Июля',
              '08': 'Августа', '09': 'Сентября', '10': 'Октября', '11': 'Ноября', '12': 'Декабря'}
list_month_keys = list(month_dict.keys())
true_answer = 0
false_answer = 0
repeat_prog = 'да'
while repeat_prog == 'да':
    for i in range(count_names):
        date_of_birth = input(f'Когда родился {select_names[i]} ? '
                              f'введите дату рождения в формате dd.mm.yyyy:')
        if date_of_birth == dict_celeb.get(select_names[i]):
            print(f'Вы угадали! {select_names[i]} родился {date_of_birth}!')
            true_answer += 1
        else:
            false_answer += 1
            for y in range(len(list_date_keys)):
                if dict_celeb.get(select_names[i]).find(list_date_keys[y], 0, 2) != -1:
                    date_find = date_dict.get(list_date_keys[y])
            for x in range(len(list_month_keys)):
                if dict_celeb.get(select_names[i]).find(list_month_keys[x], 2, 5) != -1:
                    month_find = month_dict.get(list_month_keys[x])

        print(f'{select_names[i]} родился  {date_find} {month_find} {dict_celeb.get(select_names[i])[6:]} года')
    print('Количество правильных ответов: ', true_answer)
    print('Количество не правильных ответов: ', false_answer)
    repeat_prog = input('Если хотите начать игру сначала, введите - да, если не хотите - введите нет: ')
