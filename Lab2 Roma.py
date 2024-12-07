# Лаб работа №2
# Мухамеджанов Рамазан, 100502-УБТа-о23, Вариант 2

import math
import sys

x = float(input('Введите значение х: '))
y = float(input('Введите значение y: '))
if y == 0:
    y = float(input('Выберите другое значение y: '))

f = float(input('Выберите функцию (номер): \n1) tgh(y) \n2) x^5 \n3) sqrt(x^y) \n'))
b = None

match f:
    case 1:
        f = math.tanh(y)
    case 2:
        f = x ** 5
    case 3:
        f = math.sqrt(x ** y)
    case _:
        print('Некорректный выбор функции')
        sys.exit()

if x / y > 0:
    b = math.log(f) - (f ** (1/3))
elif x / y < 0:
    b = math.log(abs(f) / y) * ((x + y) ** 3)
elif x / y == 0:
    b = (f ** 2 + y) ** 3
else:
    print('Значение не может быть вычислено')
    sys.exit()

print('Результат: ', b)