# 1. Вычислить число c заданной точностью d

d = input('Задайте точность: ')
def print_pi(d) -> float:
    pi = 3.1415926535897932384626433832
    count = 0
    for i in range(len(d)):
        count += 1

    d = float(d)

    if count > 4:
        return round(pi - d, count - 2)
    else:
        return round(pi, count - 2)


print(print_pi(d))