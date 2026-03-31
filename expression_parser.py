import ast
import basic_operations
import advanced_operations

class ExpressionParser:
    def __init__(self, memory):
        self.memory = memory  # Riceve l'oggetto memoria dal calculator.py
        
        # Mappatura operatori binari
        self.operators = {
            ast.Add: basic_operations.add,
            ast.Sub: basic_operations.sub,
            ast.Mult: basic_operations.multiply,
            ast.Div: basic_operations.divide,
            ast.Pow: advanced_operations.power,
        }

        # Mappatura funzioni testuali
        self.functions = {
            'sin': advanced_operations.sin,
            'cos': advanced_operations.cos,
            'tan': advanced_operations.tan,
            'log': advanced_operations.logarithm10,
            'ln': advanced_operations.natural_logarithm,
            'sqrt': advanced_operations.square_root,
        }

    def parse(self, expression):
        try:
            # Sostituzione estetica: ^ diventa ** per compatibilità Python
            expression = expression.strip().replace('^', '**')
            node = ast.parse(expression, mode='eval')
            return self._evaluate(node.body)
        except SyntaxError:
            return "Errore: Sintassi non valida."
        except ZeroDivisionError:
            return "Errore: Divisione per zero."
        except ValueError as e:
            return f"Errore Matematico: {str(e)}"
        except Exception as e:
            return f"Errore: {str(e)}"

    def _evaluate(self, node):
        # Costanti e numeri
        if isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.Num):
            return node.n

        # Gestione variabile ANS (richiama l'istanza della memoria)
        elif isinstance(node, ast.Name):
            if node.id.lower() == 'ans':
                return float(self.memory.get_last())
            raise ValueError(f"Variabile '{node.id}' sconosciuta.")

        # Operazioni binarie (+, -, *, /, ^)
        elif isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type in self.operators:
                left = self._evaluate(node.left)
                right = self._evaluate(node.right)
                return self.operators[op_type](left, right)

        # Chiamate a funzione (sin, cos, sqrt, ecc.)
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                func_name = node.func.id.lower()
                if func_name in self.functions:
                    args = [self._evaluate(arg) for arg in node.args]
                    return self.functions[func_name](*args)

        # Segni unari (-5, +10)
        elif isinstance(node, ast.UnaryOp):
            if isinstance(node.op, ast.USub):
                return -self._evaluate(node.operand)
            return self._evaluate(node.operand)

        raise TypeError("Espressione non riconosciuta.")