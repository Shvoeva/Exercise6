numbers = []

while True:
    output_check = input('\n\tПрекратить ввод элементов? (для выхода введите "Выйти")\n\t')
    if output_check == 'Выйти':
        break

    numbers.append(int(input('\tВведите элемент списка: ')))

print(f'\n\tСписок: {numbers}')

if numbers:
    multiplication = sum(numbers[::2]) * numbers[-1]
else:
    multiplication = 0

print(f'\tПроизведение последнего элемента исходного массива и суммы элементов с четными индексами: {multiplication}')