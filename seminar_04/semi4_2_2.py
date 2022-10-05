# Найдите корни квадратного уравнения Ax² + Bx + C = 0 
# с помощью дополнительных библиотек Python.

import cmath
  
a = float(input(" Введите значение a: ")) 
b = float(input(" Введите значение b: ")) 
c = float(input(" Введите значение c: ")) 
  
dis_form = (b**2) - (4 * a*c)
  
res1 = (-b - cmath.sqrt(dis_form))/(2 * a)
res2 = (-b + cmath.sqrt(dis_form))/(2 * a)
  
print(res1)
print(res2)