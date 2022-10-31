from calculator import sum
from calculator import diff
from calculator import mult

def test_sum_good():
    assert sum(10, 5) == 15

def test_diff_good():
    assert diff(10, 5) == 5

def test_mult_good():
    assert mult(10, 5) == 50        
