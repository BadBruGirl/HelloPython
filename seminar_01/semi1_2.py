# 2 Найти максимальное из пяти чисел.
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
d = int(input('Введите четвертое число: '))
e = int(input('Введите пятое число: '))

list = [a, b, c, d, e]
i = 0
while i < len(list)-1:
    if list[i] > list[i+1]:
        max = list[i]
        i += 1
    else:
        max = list[i+1]
    i += 1
print('Максимальное число = ', max)