# Handle the last result and the history of calculations
class Memory:
    def __init__(self):
        self.history = []
        self.last_result = 0

    def save(self, expression, result):
        self.last_result = result
        self.history.append(f"{expression} = {result}")

    def get_last(self):
        return self.last_result

    def show_history(self):
        return "\n".join(self.history) if self.history else "Empty history."
