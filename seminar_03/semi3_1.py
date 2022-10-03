# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора
# псевдослучайных чисел.

import datetime 

min_n = 10
max_n = 100

def randomer():
    return datetime.datetime.now().microsecond%10

n = randomer()

print(int(len(str(min_n))))
print(n) 