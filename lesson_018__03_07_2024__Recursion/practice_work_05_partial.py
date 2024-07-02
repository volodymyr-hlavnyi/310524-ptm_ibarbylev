"""Напишите программу, которая использует метод functools.partial для создания функции
binary_to_decimal, которая принимает строку, представляющую двоичное число,
и возвращает его десятичное представление.
Используйте функцию int в качестве базовой функции,
но зафиксируйте аргумент base со значением 2 с помощью partial.
Выведите результат на экран.

Пример:

"101010"  -> 42

Подсказка:
Используйте функцию int() с base=2:
int("101010", base=2): 42
"""

from functools import partial

# ============ variant 1 ================
# binary_to_decimal = partial(int, base=2)


# ============ variant 2 ================
def binary_to_decimal(binary_str: str) -> int:
    return partial(int, base=2)(binary_str)


print(binary_to_decimal("101010"))

