# 3 Дан файл jack.txt (https://disk.yandex.ru/d/orFlUSXkcA600w)
# по аналогии с предыдущим заданием составить аналогичный словарь.

import collections

with open("jack.txt", "r", encoding='utf-8') as datafile:
    lines = datafile.read()
    words = lines.split()
    words_hist = collections.Counter(words)
    print (words_hist)

