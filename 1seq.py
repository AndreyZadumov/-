numbers = int(input('Введите количество элементов списка: '))
list_of_numbers = list()
for i in range(1,numbers +1):
    el = int(input(f'Введите {i} элемент: '))
    list_of_numbers.append(el)
list_of_numbers.sort()
print(list_of_numbers)
