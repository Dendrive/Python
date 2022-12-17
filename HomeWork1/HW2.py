#Напишите программу для проверки ложности утверждения
#¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

predic = [True, False]
for x in predic:
    for y in predic:
        for z in predic:
            res = not (x or y or z) == (not x) and (not y) and (not z)
            print(x, y, z)