# Задание 1. 
my_str = 'абв иеква роеабв абв нкниср ываыуабв'

new_str = ' '.join(list(filter(lambda elem: 'абв' not in elem.lower(), my_str.split())))

print(new_str)