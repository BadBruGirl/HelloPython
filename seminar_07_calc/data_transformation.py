import console as c_ui
from fractions import Fraction
import cmath
from calculator import Calc_block as c_calc
import data_transformation as d_t


def data_formatting(data):
    data_type, first_value, oper, second_value = data

    if data_type == '1':

        first_value = complex(first_value)

        second_value = complex(second_value)

    elif data_type == '2':

        a = first_value
        first_value = Fraction(int(a[0: a.index(
            '/')]), int(a[a.index('/')+1:len(a)]))

        g = second_value
        second_value = Fraction(int(g[0: g.index(
            '/')]), int(g[g.index('/')+1:len(g)]))

    return (first_value, oper, second_value)