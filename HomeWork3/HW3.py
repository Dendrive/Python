a = int(input('Введите положительное число: '))


def dvoich(n: int):
    if n > 0:
        d = n % 2
        dvoich(n // 2)
        print(d, end='')


if a <= 0:
    print('Попробуй ещё раз!')
else:
    dvoich(a)