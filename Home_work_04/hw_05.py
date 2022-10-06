# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача -
# сформировать файл, содержащий сумму многочленов.

with open('mnogochlen_stepeni_k.txt', 'r') as file:
   mnog1 = file.read()
   mnog1 = mnog1[0:-4]

with open('mnogochlen2.txt', 'r') as file:
   mnog2 = file.read()

with open('sum_mnogochlenov.txt', 'w', encoding='utf-8') as file:
   file.write(f'{mnog1} + {mnog2}')