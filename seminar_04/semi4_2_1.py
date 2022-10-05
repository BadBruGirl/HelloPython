# Найдите корни квадратного уравнения Ax² + Bx + C = 0 
# с помощью математических формул нахождения корней квадратного уравнения;

import math 

# функция для нахождения корней
def findRoots(a, b, c): 
 
    dis_form = b * b - 4 * a * c 
    sqrt_val = math.sqrt(abs(dis_form)) 
 
    if dis_form > 0: 
        print(" корни действительны и различны ") 
        print((-b + sqrt_val) /(2 * a)) 
        print((-b - sqrt_val) /(2 * a)) 
 
    elif dis_form == 0: 
        print(" оба корня одинаковы ") 
        print(-b /(2 * a)) 
 
 
    else: 
        print(" комплексные корни ") 
        print(- b /(2 * a), " + i", sqrt_val) 
        print(- b /(2 * a), " - i", sqrt_val) 
 
 
a = float(input(" Введите значение a: ")) 
b = float(input(" Введите значение b: ")) 
c = float(input(" Введите значение c: ")) 
 
# Если ввеедено значение а = 0, то уравнение неверное
if a == 0: 
    print(" Введите корректное значение ") 
 
else: 
    findRoots(a, b, c) 