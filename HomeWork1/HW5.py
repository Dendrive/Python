# Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = pow(x2 - x1, 2)
y = pow(y2 - y1, 2)
result = (pow(x + y, 0.5))
print(round(result, 3))



