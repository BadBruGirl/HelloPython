# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def sum_num_odd_index(list):
    sum = 0
    for i in range(len(list)):
        if i % 2 != 0:
            sum += list[i]
    print(f"Сумма равна: {sum}")

list = [8, 12, 88, 73, 75, 2]
sum_num_odd_index(list)

