# 2.Задача 1 из домашней работы 3. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

numbers_list = list(map(int, input("Введите числа через пробел:\n").split()))
sum_odd = sum(numbers_list[item] for item in range(1, len(numbers_list), 2))
odd_el = str([numbers_list[item] for item in range(1, len(numbers_list), 2)]).strip('[]')
print(f'Для списка {numbers_list} сумма чисел, стоящих на нечётных позициях: \n{odd_el} равна {sum_odd}.')