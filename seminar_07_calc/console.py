def view_data(data, title):
    print(f'{title} = {data}')

def get_value():
    return input()


def input_data():
    print('Введите 1 для работы с комплексными числами, 2 - для работы с рациональными числами')
    data_type = get_value()
    if data_type == '1':
        print('Введите первое число (используйте формат: "5 + 3j"):')
        first_value = get_value()
        print('Введите второе число (используйте формат: "5 + 3j"):')
        second_value = get_value()
        print('Выберите операцию:')
        oper = get_value()
    elif data_type == '2':
        print('Введите первое число (используйте формат: "5/11"):')
        first_value = get_value()
        print('Введите второе число (используйте формат: "5/11"):')
        second_value = get_value()
        print('Выберите операцию пользуясь символами: " + , - , /, * " ')
        oper = get_value()
    return (data_type, first_value, oper, second_value)