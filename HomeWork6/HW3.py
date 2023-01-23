# Задание 3.
from itertools import groupby


def dictionary(*args):
    if "" not in args:
        return {k: list(names) for k, names in groupby(sorted(args), key=lambda i: i[0]) if k}
    return "Error"


print(dictionary("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"))