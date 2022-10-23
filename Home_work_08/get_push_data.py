def summa(a):
    result = ''
    for i in range(3):
        result += a[i]
    return result.replace('\n', '') + '\n'

def get_data():
    with open('name.csv', 'r', encoding='UTF-8') as name:
        name = name.readlines()

    with open('class.csv', 'r', encoding='UTF-8') as classe:
        classe = classe.readlines()

    with open('adress.csv', 'r', encoding='UTF-8') as adress:
        adress = adress.readlines()

    list = [summa(i) for i in zip(name, classe, adress)]
    return list

def push_data(strk):
    strk = strk.split(';') # разделяем строку
    with open('name.csv', 'a', encoding='UTF-8') as name:
        for i in range(0, 5):
            name.write(strk[i] + ';')
        name.write('\n')

    with open('class.csv', 'a', encoding='UTF-8') as classe:
        classe.write(strk[0] + ';')
        for i in range(5, 7):
            classe.write(strk[i] + ';')
        classe.write('\n')

    with open('adress.csv', 'a', encoding='UTF-8') as adress:
        adress.write(strk[0] + ';')
        for i in range(7, 12):
            adress.write(strk[i] + ';')
        adress.write('\n')