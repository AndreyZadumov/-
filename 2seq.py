numbers = input('Введите элементы списка через заятую: ')

numbers = list(numbers)
for i in numbers:
    if i ==',' or i == '/' or i == ';':
        numbers.remove(i)
print(list(set(numbers)))

