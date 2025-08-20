# Agente Cognitivo com Grafo de Conhecimento

Este repositório contém uma implementação simples de um **Agente Cognitivo** em Python, que constrói e gerencia um **grafo de conhecimento** usando a biblioteca [NetworkX](https://networkx.org/). O agente permite adicionar relações entre entidades, consultar conexões lógicas entre elas e visualizar o grafo resultante.

## 📁 Arquivo principal

- `main.py` — Código principal contendo a definição do agente, inserção de conhecimento, consultas e visualização.

## 🚀 Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/vitor-souza-ime/ac.git
cd ac
````

### 2. Instale as dependências

Certifique-se de ter o Python 3 instalado. Para instalar as bibliotecas necessárias, utilize:

```bash
pip install -r requirements.txt
```

> Caso o arquivo `requirements.txt` não esteja presente, instale diretamente:
>
> ```bash
> pip install networkx matplotlib
> ```

### 3. Execute o código

```bash
python main.py
```

Isso irá:

* Construir um grafo de conhecimento com 28 relações entre diferentes entidades.
* Realizar consultas sobre as conexões entre algumas entidades específicas.
* Exibir o grafo visualmente com rótulos e direções.

## 🧠 Exemplo de Consulta

O agente é capaz de responder se existe um caminho relacional entre duas entidades e quais relações ligam essas entidades. Por exemplo:

```python
agente.consultar_relacao("Gato", "Alimentação")
# Saída: Existe um caminho entre 'Gato' e 'Alimentação' com as relações: é um tipo de -> precisa de
```

## 📊 Visualização

O grafo gerado é exibido usando `matplotlib`, com:

* Nós representando entidades (como "Cachorro", "Animal", "Via Láctea")
* Arestas direcionadas com rótulos representando as relações (como "é um tipo de", "faz", "tem")

## 📌 Estrutura do Grafo

O agente utiliza um **grafo direcionado** (`DiGraph`), o que significa que as relações têm direção (de entidade origem para entidade destino).

## 💡 Possíveis melhorias

* Implementar um sistema de inferência lógica baseado nas relações.
* Suportar relações bidirecionais ou simétricas.
* Exportar/importar o grafo em formatos como GraphML ou JSON.

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

