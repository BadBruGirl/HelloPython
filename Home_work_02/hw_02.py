# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

number = int(input("Пусть N = "))
factorial = 1
for i in range(1, number+1):
    factorial *= i
    print(factorial, end=' ')
