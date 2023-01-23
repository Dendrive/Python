# Задание 2.
num = int(input("Введите длину списка N: "))
def multipl_list(num: int):
    a = [i for i in range(20, num + 1) if i % 20 == 0 or i % 21 == 0]
    return a
print()
print(f"Список чисел в пределах от 20 до N, кратных 20 и 21:\n {multipl_list(num)}")
print()