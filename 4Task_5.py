"""5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce()."""

from random import randint
from functools import reduce


my_list = [i for i in range(99, 1001) if i % 2 == 0]
result = reduce(lambda x,y: x * y, my_list)
print(my_list)
print(result)
