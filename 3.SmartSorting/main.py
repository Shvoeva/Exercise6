list_numbers = []

while True:
    output_check = input('\n\tПрекратить ввод элементов? (для выхода введите "Выйти")\n\t')
    if output_check == 'Выйти':
        break

    list_numbers.append(int(input('\tВведите элемент списка: ')))

tuple_numbers = tuple(list_numbers)
print(f'\n\tКортеж: {tuple_numbers}')

sorting_numbers = sorted(tuple_numbers, key=lambda number: abs(number))

print(f'\tОтсортированный кортеж по абсолютным значениям в возрастающем порядке: {sorting_numbers}')