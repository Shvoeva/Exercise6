list_numbers = []
while True:
    list_numbers.append(int(input('\n\tВведите элемент списка: ')))

    output_check = input('\tПрекратить ввод элементов? '
                         '(для выхода введите "Выйти")\n\t')
    if output_check == 'Выйти':
        break

print(f'\n\tСписок: {list_numbers}')

sorting_numbers = sorted(list_numbers)
len_numbers = len(sorting_numbers)
half_length_list = len_numbers // 2
if len_numbers % 2 == 1:
    median = sorting_numbers[half_length_list]
else:
    median = (sorting_numbers[half_length_list - 1]
              + sorting_numbers[half_length_list]) / 2

print(f'\tМедиана массива: {median}')