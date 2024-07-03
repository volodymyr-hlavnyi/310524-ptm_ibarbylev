"""Это хвостовая рекурсия (tail recursion) или не хвостовая (non-tail recursion)?

    def sum_list(lst):
        if not lst:
            return 0
        return lst[0] + sum_list(lst[1:])

Как преобразовать её в рекурсию (не) хвостового типа?
"""


def sum_list_tail_recursion(lst, accumulator=0):
    if not lst:
        return accumulator
    return sum_list_tail_recursion(lst[1:],  lst[0] + accumulator)


nums = [1, 2, 3, 4, 5]
print(sum_list_tail_recursion([1, 2, 3, 4, 5]))  # 15
