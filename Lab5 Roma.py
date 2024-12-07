# Лаб работа №5
# Мухамеджанов Рамазан, 100502-УБТа-о23, Вариант 2

# Задание 1
numbers = input('Введите целые числа через пробел: ', ).split()
numbers = [int(num) for num in numbers]

min_num = min(numbers)
index_min = numbers.index(min_num)

print('Минимальный элемент в списке: ', min_num, '\nИндекс минимального элемента: ', index_min)

# Задание 2
numbers = input('Введите целые числа через пробел: ', ).split()
numbers = [int(num) for num in numbers]

numbers2 = []
numbers3 = []

for num in numbers:
    if num > 0:
        numbers2.append(num)
    else:
        numbers3.append(num)
print('Второй список: ', numbers2, '\nТретий список: ', numbers3)