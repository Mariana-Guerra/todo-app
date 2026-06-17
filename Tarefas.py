class Tarefas:
    def _init_(self):
        self.lista = [ ]

def adicionar(self, nome):
  self. lista. append ({
     "nome": nome,
"concluida": False
  })

def listar(self):
    for i, t in enumerate(self.lista, 1):
        s = "V" if t["concluida"] else "o"
        print(f"{i}. [{s}] {t['nome']}")

def adicionar(self, nome, prioridade="normal"):
     self.lista.append({
            "nome": nome,
            "concluida": False,
            "prioridade": prioridade
        })

def listar(self):
        if not self.lista:
            print("Nenhuma tarefa cadastrada.")
            return
        for i, t in enumerate(self.lista, 1):
            s = "✓" if t["concluida"] else "○"
            p = t.get("prioridade", "normal")
            print(f"{i}. [{s}] {t['nome']} ({p})")