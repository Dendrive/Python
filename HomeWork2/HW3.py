# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

n = int(input("Введите число: "))
my_dict = {}
sum = 0
for i in range(1, n + 1):
    my_dict[i] = round((1 + 1 / i)**i, 2)
    sum += round((1 + 1 / i)**i, 2)
print(my_dict)
print(sum)
