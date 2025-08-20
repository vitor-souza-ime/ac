import networkx as nx
import matplotlib.pyplot as plt

class AgenteCognitivo:
    def __init__(self):
        self.grafo_conhecimento = nx.DiGraph()

    def adicionar_conhecimento(self, entidade1, relacao, entidade2):
        self.grafo_conhecimento.add_edge(entidade1, entidade2, relacao=relacao)

    def consultar_relacao(self, entidade1, entidade2):
        if nx.has_path(self.grafo_conhecimento, entidade1, entidade2):
            caminho = nx.shortest_path(self.grafo_conhecimento, entidade1, entidade2)
            relacoes = []
            for i in range(len(caminho)-1):
                relacoes.append(self.grafo_conhecimento[caminho[i]][caminho[i+1]]['relacao'])
            return f"Existe um caminho entre '{entidade1}' e '{entidade2}' com as relações: {' -> '.join(relacoes)}"
        else:
            return f"Nenhum caminho encontrado entre '{entidade1}' e '{entidade2}'."

    def mostrar_grafo(self):
        pos = nx.spring_layout(self.grafo_conhecimento, seed=42)
        plt.figure(figsize=(12,9))
        nx.draw(self.grafo_conhecimento, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold', arrowsize=20)
        edge_labels = nx.get_edge_attributes(self.grafo_conhecimento, 'relacao')
        nx.draw_networkx_edge_labels(self.grafo_conhecimento, pos, edge_labels=edge_labels, font_color='red', font_size=8)
        plt.title("Grafo de Conhecimento do Agente Cognitivo")
        plt.show()


agente = AgenteCognitivo()

# Conhecimento inicial expandido com 20 relações
conhecimentos = [
    ("Cachorro", "é um tipo de", "Animal"),
    ("Animal", "tem", "Patas"),
    ("Cachorro", "faz", "Latido"),
    ("Gato", "é um tipo de", "Animal"),
    ("Gato", "faz", "Miado"),
    ("Pata", "é parte de", "Cachorro"),
    ("Pata", "é parte de", "Gato"),
    ("Ave", "é um tipo de", "Animal"),
    ("Pássaro", "é um tipo de", "Ave"),
    ("Pássaro", "faz", "Canto"),
    ("Peixe", "é um tipo de", "Animal"),
    ("Peixe", "vive em", "Água"),
    ("Água", "cobre", "Terra"),
    ("Terra", "é planeta", "Sistema Solar"),
    ("Sistema Solar", "está na", "Via Láctea"),
    ("Via Láctea", "é uma", "Galáxia"),
    ("Galáxia", "é parte de", "Universo"),
    ("Cachorro", "tem", "Rabo"),
    ("Gato", "tem", "Rabo"),
    ("Rabo", "é usado para", "Equilíbrio"),
    ("Pássaro", "tem", "Asas"),
    ("Asas", "são usadas para", "Voar"),
    ("Peixe", "tem", "Nadadeiras"),
    ("Nadadeiras", "são usadas para", "Nadar"),
    ("Animal", "precisa de", "Alimentação"),
    ("Cachorro", "come", "Ração"),
    ("Gato", "come", "Peixe"),
    ("Peixe", "come", "Alimento Aquático"),
]

for tripla in conhecimentos:
    agente.adicionar_conhecimento(*tripla)

# Consultas adicionais
consultas = [
    ("Pássaro", "Terra"),
    ("Cachorro", "Sistema Solar"),
    ("Peixe", "Equilíbrio"),
    ("Gato", "Alimentação"),
    ("Cachorro", "Patas"),
    ("Gato", "Latido"),
]

# Exibir respostas das consultas
for e1, e2 in consultas:
    print(agente.consultar_relacao(e1, e2))

# Mostrar grafo ampliado
agente.mostrar_grafo()
