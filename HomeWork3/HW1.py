my_list = []

l = int(input('Введите длину списка: '))

for i in range(l):
    my_list.append(int(input('Введите число: ')))
print(my_list)

def find_and_sum(a_list: list):
    sum_index = 0
    for i in range(len(a_list)):
        if i % 2 != 0:
            sum_index += a_list[i]
    print(sum_index)

find_and_sum(my_list)

