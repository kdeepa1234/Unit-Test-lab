
import pytest
from calculator import add, subtract, multiply, divide

def test_addition():
    assert add(5, 5) == 10

def test_subtraction():
    assert subtract(10, 5) == 5

def test_multiplication():
    assert multiply(4, 5) == 20

def test_division():
    assert divide(20, 4) == 5

def test_division_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
