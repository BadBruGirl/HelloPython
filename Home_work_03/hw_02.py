# 2.Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

list = [2, 3, 4, 5, 6, 0]
result_list = []
for i in range((len(list)+1)//2):
    result_list.append(list[i]*list[len(list)-1-i])
print(result_list)