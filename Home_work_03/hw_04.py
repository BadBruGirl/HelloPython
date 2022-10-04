# 4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# print(bin(45)) # встроенная функция в Python

number = int(input('Введите число: ')) 
bin = ''
while number > 0:
    bin = str(number % 2) + bin
    number = number // 2
print(f'Двоичное число1: {bin}')