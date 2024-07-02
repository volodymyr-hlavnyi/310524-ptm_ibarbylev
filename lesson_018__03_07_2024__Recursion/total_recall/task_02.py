"""Дана функция numbers_squared.
Перепишите её как лямбда-функцию numbers_squared_lambda.
"""


def numbers_squared(lst: list[int]) -> list[int]:
    new_lst = []
    for item in lst:
        new_lst.append(item ** 2)

    return new_lst


lst = [1, 2, 3]
print(numbers_squared(lst))   # [1, 4, 9]

numbers_squared_lambda = ...
