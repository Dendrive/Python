# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.

num = float(input())
if num < 0:
    num *= -1
while num != int(num):
    num = round(num * 10, 10)
sum = 0
c = 0
while 0 < num:
    c = num % 10
    sum = c + sum
    num = num // 10
print(round(sum))

