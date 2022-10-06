# 2 Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.

num = int(input("Введите число: "))
i = 2 
list = []
old_num = num
while i <= num:
    if num % i == 0:
        list.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old_num} приведены в списке: {list}")