# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее
# кратное) этих двух чисел.

x, y = 4, 6
if x > y: larger_num = x
else: larger_num = y
while(True):
    if (larger_num % x == 0) and (larger_num % y == 0):
        result = larger_num
        break
    larger_num += 1
print(result)