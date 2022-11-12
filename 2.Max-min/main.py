numbers = []

while True:
    output_check = input('\n\tПрекратить ввод элементов? (для выхода введите "Выйти")\n\t')
    if output_check == 'Выйти':
        break

    numbers.append(float(input('\tВведите элемент списка: ')))

print(f'\n\tСписок: {numbers}')

if numbers:
    difference = max(numbers) - min(numbers)
else:
    difference = 0

print('\tРазница между максимумом и минимумом элементов: {0:.3f}'.format(difference))