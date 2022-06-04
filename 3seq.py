first_list = input('Введите элементы 1-го списка: ')
first_list = list(first_list)
for i in first_list:
    if i ==',' or i == '/' or i == ';':
        first_list.remove(i)
second_list = input('Введите элементы 2-го списка: ')
second_list = list(second_list)
for i in second_list:
    if i ==',' or i == '/' or i == ';':
        second_list.remove(i)
difference = []
for i in first_list:
    if not (i in second_list):
        difference.append(i)
print(difference)
