import pytest
from unittest.mock import patch
from expression_parser import ExpressionParser

def test_simple_addition():
    parser = ExpressionParser()
    assert parser.parse("3 + 4") == 7

def test_simple_subtraction():
    parser = ExpressionParser()
    assert parser.parse("5 - 4") == 1

def test_simple_multiplication():
    parser = ExpressionParser()
    assert parser.parse("3 * 4") == 12

def test_simple_division():
    parser = ExpressionParser()
    assert parser.parse("16 / 4") == 4

def test_operator_precedence():
    parser = ExpressionParser()
    # La moltiplicazione deve avvenire prima dell'addizione
    assert parser.parse("2 + 3 * 4") == 14

def test_parentheses():
    parser = ExpressionParser()
    # Le parentesi alterano la precedenza
    assert parser.parse("(2 + 3) * 4") == 20

def test_nested_parentheses():
    parser = ExpressionParser()
    assert parser.parse("((10 - 4) / 2) + 3") == 6

def test_unary_negative():
    parser = ExpressionParser()
    assert parser.parse("-5 + 10") == 5

def test_unary_negative_with_parentheses():
    parser = ExpressionParser()
    assert parser.parse("10 * (-2)") == -20

def test_zero_division_error():
    parser = ExpressionParser()
    # Il parser restituisce una stringa di errore, quindi controlliamo il testo
    risultato = parser.parse("10 / 0")
    assert "Errore" in risultato

def test_syntax_error():
    parser = ExpressionParser()
    # Testiamo una sintassi palesemente errata
    risultato = parser.parse("5 + * 3")
    assert "Errore di Sintassi" in risultato

# I decoratori ora puntano correttamente al file 'expression_parser'
@patch('expression_parser.Memory.get_last')
def test_ans_addition(mock_get_last):
    mock_get_last.return_value = 10.0
    parser = ExpressionParser()
    assert parser.parse("ans + 5") == 15.0

@patch('expression_parser.Memory.get_last')
def test_ans_in_complex_expression(mock_get_last):
    mock_get_last.return_value = 5.0
    parser = ExpressionParser()
    assert parser.parse("2 * (ans + 3)") == 16.0