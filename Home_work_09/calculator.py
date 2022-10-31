# код для расчетов операций
import cmath

def Calc_block(data):
    first_value, oper, second_value = data
    if oper == '+':
        return sum(first_value, second_value)
    if oper == '-':
        return diff(first_value, second_value)
    if oper == '*':
        return mult(first_value, second_value)
    if (oper =='/') and (second_value != 0):
        return div(first_value, second_value)
    else:
        return 'На 0 не делим!'

def sum(first_value, second_value):
    return first_value + second_value

def diff(first_value, second_value):
    return first_value - second_value

def mult(first_value, second_value):
    return first_value * second_value

def div(first_value, second_value):
    return first_value / second_value
