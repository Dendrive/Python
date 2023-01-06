k = int(input('Введите число: '))


def print_iterator(gen):
    for x in gen:
        print(x, end=' ')


def negofibonacci(n: int):
    a, b = 0, 1

    for i in range(-n - 1, 0):
        yield a
        a, b = b, a - b


lst = list(negofibonacci(k))
result = reversed(lst)
print_iterator(result)


def fibonacci(n: int):
    a, b = 1, 1

    for i in range(0, n):
        yield a
        a, b = b, a + b


data = list(fibonacci(k))
print_iterator(data)