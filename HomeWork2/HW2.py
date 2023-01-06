# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.

a = int(input("Input your number, please: "))
b = 1
c = 1
for b in range(1, a + 1):
    c = c * b
    print(c, end = ' ')