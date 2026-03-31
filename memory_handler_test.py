from memory_handler import Memory  
import pytest

class TestMemory:

    def test_initial_state(self):
        """Verifica che la memoria sia vuota all'inizializzazione."""
        mem = Memory()
        assert mem.last_result == 0
        assert mem.get_last() == 0
        assert mem.show_history() == "Empty history."

    def test_save_and_get_last(self):
        """Verifica che il salvataggio aggiorni l'ultimo risultato."""
        mem = Memory()
        mem.save("2 + 2", 4)
        assert mem.get_last() == 4
        
        mem.save("5 * 2", 10)
        assert mem.get_last() == 10

    def test_history_logging(self):
        """Verifica che la cronologia formatti correttamente le operazioni."""
        mem = Memory()
        mem.save("10 / 2", 5.0)
        mem.save("3 + 3", 6)
        
        history = mem.show_history()
        expected_history = "10 / 2 = 5.0\n3 + 3 = 6"
        assert history == expected_history

    def test_sequential_saves(self):
        """Verifica che più salvataggi consecutivi vengano mantenuti correttamente."""
        mem = Memory()
        operazioni = [("1+1", 2), ("2+2", 4), ("3+3", 6)]
        
        for expr, res in operazioni:
            mem.save(expr, res)
            
        history_lines = mem.show_history().split("\n")
        assert len(history_lines) == 3
        assert history_lines[0] == "1+1 = 2"
        assert history_lines[-1] == "3+3 = 6"

    def test_get_last_without_saves(self):
        """Verifica il comportamento di get_last su un'istanza nuova."""
        mem = Memory()
        assert mem.get_last() == 0