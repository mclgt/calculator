import pytest
from unittest.mock import patch
from expression_parser import ExpressionParser
from memory_handler import Memory

def test_simple_addition():
    memory = Memory()
    parser = ExpressionParser(memory)
    assert parser.parse("3 + 4") == 7

def test_simple_subtraction():
    memory = Memory()
    parser = ExpressionParser(memory)
    assert parser.parse("5 - 4") == 1

def test_simple_multiplication():
    memory = Memory()
    parser = ExpressionParser(memory)
    assert parser.parse("3 * 4") == 12

def test_simple_division():
    memory = Memory()
    parser = ExpressionParser(memory)
    assert parser.parse("16 / 4") == 4

def test_operator_precedence():
    memory = Memory()
    parser = ExpressionParser(memory)
    assert parser.parse("2 + 3 * 4") == 14

def test_parentheses():
    memory = Memory()
    parser = ExpressionParser(memory)
    assert parser.parse("(2 + 3) * 4") == 20

def test_nested_parentheses():
    memory = Memory()
    parser = ExpressionParser(memory)
    assert parser.parse("((10 - 4) / 2) + 3") == 6

def test_unary_negative():
    memory = Memory()
    parser = ExpressionParser(memory)
    assert parser.parse("-5 + 10") == 5

# --- NUOVI TEST AVANZATI ---

def test_power_with_caret():
    memory = Memory()
    parser = ExpressionParser(memory)
    assert parser.parse("2 ^ 3") == 8.0

def test_square_root():
    memory = Memory()
    parser = ExpressionParser(memory)
    assert parser.parse("sqrt(16)") == 4.0

def test_trigonometry_sin():
    memory = Memory()
    parser = ExpressionParser(memory)
    assert parser.parse("sin(90)") == 1.0

def test_logarithm():
    memory = Memory()
    parser = ExpressionParser(memory)
    assert parser.parse("log(100)") == 2.0

def test_natural_logarithm():
    memory = Memory()
    parser = ExpressionParser(memory)
    assert parser.parse("ln(1)") == 0.0

# --- TEST ERRORI ---

def test_zero_division_error():
    memory = Memory()
    parser = ExpressionParser(memory)
    risultato = parser.parse("10 / 0")
    assert "Errore" in risultato

def test_syntax_error():
    memory = Memory()
    parser = ExpressionParser(memory)
    risultato = parser.parse("5 + * 3")
    assert "Errore" in risultato

def test_sqrt_negative_error():
    memory = Memory()
    parser = ExpressionParser(memory)
    risultato = parser.parse("sqrt(-1)")
    assert "Errore Matematico" in risultato

# --- TEST MEMORIA (ans) ---

@patch('memory_handler.Memory.get_last')
def test_ans_addition(mock_get_last):
    mock_get_last.return_value = 10.0
    memory = Memory()
    parser = ExpressionParser(memory)
    assert parser.parse("ans + 5") == 15.0

@patch('memory_handler.Memory.get_last')
def test_ans_in_complex_expression(mock_get_last):
    mock_get_last.return_value = 5.0
    memory = Memory()
    parser = ExpressionParser(memory)
    assert parser.parse("2 * (ans + 3)") == 16.0