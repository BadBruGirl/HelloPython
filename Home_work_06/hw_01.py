# 1. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

numbers_list = list(map(int, input("Введите числа через пробел:\n").split()))
result_list = list(filter(lambda a: numbers_list.count(a) == 1, numbers_list))
print(f'Для последовательности {numbers_list}, \n Список неповторяющихся элементов элементов => {result_list}')