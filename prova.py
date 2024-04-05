from flask import Flask, jsonify, request
import queue

app = Flask(__name__)

class Fila:
    def __init__(self):
        self.fila = queue.Queue()

    def enfileirar(self, elemento):
        self.fila.put(elemento)

    def desenfileirar(self):
        self.fila.get()
    
    def estaVazia(self):
        self.fila.empty()
        

class RoboDeLimpeza:

    def __init__(self):
        self.filaDeLimpeza = Fila()
        self.tarefasExecutadas = []

    def adicionarTarefa(self,tarefa):
        self.filaDeLimpeza.enfileirar(tarefa)

    def executarProximaTarefa(self):
        if not self.filaDeLimpeza.estaVazia():
            proxima_tarefa = self.filaDeLimpeza.desenfileirar()
            print(proxima_tarefa)
            self.tarefasExecutadas.append(proxima_tarefa)
        else:
            print("Não há tarefas na fila")

    def executarTodasTarefas(self):
        while self.filaDeLimpeza.estaVazia():
            self.executarProximaTarefa()
            

@app.route('/', methods=['GET'])
def executar_tarefas():
    if not Jorge.filaDeLimpeza.estaVazia():
        return jsonify(message="Todas as tarefas foram executadas com sucesso.", tarefasExecutadas = {Jorge.tarefasExecutadas}, status=200)
    else:
        return jsonify(message="Não há tarefas pendentes a serem executadas", tarefasExecutadas = {Jorge.tarefasExecutadas}, status=204)
    
if __name__ == "__main__":
   Jorge = RoboDeLimpeza()
app.run(debug=True, port = 4321)
