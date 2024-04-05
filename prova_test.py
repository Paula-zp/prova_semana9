import queue
from prova import RoboDeLimpeza

def test_adicionar():
    Jorge = RoboDeLimpeza()
    Jorge.adicionarTarefa("Escovar")
    assert Jorge.listaDeLimpeza == "Escovar", "Foi adicionado"