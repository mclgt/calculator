import advanced_operations 
import pytest
import math

# Power Test
def test_positive_power():
    assert advanced_operations.power(2,3)==8    
def test_negative_power():
    assert advanced_operations.power(-2,3)==-8
def test_zero_power():
    assert advanced_operations.power(5,0)==1
def test_fractional_power():
    assert advanced_operations.power(9,0.5)==3  

# Square Root Test
def test_positive_square_root():
    assert advanced_operations.square_root(16)==4       
def test_zero_square_root():
    assert advanced_operations.square_root(0)==0    
def test_negative_square_root():
    with pytest.raises(ValueError):
        advanced_operations.square_root(-1)

# Logarithm Test
def test_positive_logarithm10():
    assert advanced_operations.logarithm10(100)==2
def test_zero_logarithm10():
    with pytest.raises(ValueError):
        advanced_operations.logarithm10(0)
def test_negative_logarithm10():
    with pytest.raises(ValueError):
        advanced_operations.logarithm10(-10)

def test_positive_natural_logarithm():
    assert advanced_operations.natural_logarithm(math.e)==1 
def test_zero_natural_logarithm():
    with pytest.raises(ValueError):
        advanced_operations.natural_logarithm(0)
def test_negative_natural_logarithm():
    with pytest.raises(ValueError):
        advanced_operations.natural_logarithm(-5)

# Trigonometric Test
def test_sin():
    assert round(advanced_operations.sin(30), 5) == 0.5 
    assert round(advanced_operations.sin(90), 5) == 1.0
def test_cos():
    assert round(advanced_operations.cos(60), 5) == 0.5
    assert round(advanced_operations.cos(90), 5) == 0.0
def test_tan():
    assert round(advanced_operations.tan(45), 5) == 1.0
    assert round(advanced_operations.tan(0), 5) == 0.0

