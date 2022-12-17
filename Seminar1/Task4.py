# 4. Напишите программу, которая будет принимать на вход дробь
# и показывать первую цифру дробной части числа.

def chek_first_num():
    number = float(input("Input your number"))
    new_num = int(number * 10 % 10)
    print(new_num)
chek_first_num()