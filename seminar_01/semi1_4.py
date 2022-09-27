# 4 Показать первую цифру дробной части числа.
num = float(input("Введите дробное число: "))
round_num = int(num)
result = (num - round_num) * 10
print(f'Первая цифра дробной части: {int(result)}')
