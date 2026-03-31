import ast
import basic_operations
from memory_handler import Memory

class ExpressionParser:
    def __init__(self):
        self.operators = {
            ast.Add: basic_operations.add,
            ast.Sub: basic_operations.sub,
            ast.Mult: basic_operations.multiply,
            ast.Div: basic_operations.divide,
        }

    def parse(self, expression):
        try:
            expression = expression.strip()
            node = ast.parse(expression, mode='eval')
            return self._evaluate(node.body)
            
        except SyntaxError:
            return "Errore di Sintassi: Controlla le parentesi e l'ordine degli operatori."
        except ZeroDivisionError:
            return "Errore: Impossibile dividere per zero."
        except Exception as e:
            return f"Errore durante il calcolo: {str(e)}"

    def _evaluate(self, node):
        # 1. Numeri semplici
        if isinstance(node, ast.Constant):
            return node.value

        # 2. Variabile 'ans'
        elif isinstance(node, ast.Name):
            if node.id.lower() == 'ans':
                return float(Memory.get_last())
            raise ValueError(f"Variabile '{node.id}' non riconosciuta. Usa solo 'ans'.")

        # 3. Operazioni matematiche binarie (+, -, *, /)
        elif isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type in self.operators:
                left_val = self._evaluate(node.left)
                right_val = self._evaluate(node.right)
                # CHIAMIAMO LA FUNZIONE DIRETTAMENTE (senza .execute)
                return self.operators[op_type](left_val, right_val)
            raise ValueError("Operatore matematico non supportato.")

        # 4. Segni unari (es. -5 o +3)
        elif isinstance(node, ast.UnaryOp):
            if isinstance(node.op, ast.USub): 
                return -self._evaluate(node.operand)
            elif isinstance(node.op, ast.UAdd): 
                return self._evaluate(node.operand)
        raise TypeError("Struttura non valida nell'espressione.")