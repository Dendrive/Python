# Задание 1.
original_list = [15, 16, 2, 3, 1, 7, 5, 4, 10]
print(original_list)
new_list = [num for i, num in enumerate(original_list) if i > 0 and original_list[i] > original_list[i - 1]]
print(new_list)