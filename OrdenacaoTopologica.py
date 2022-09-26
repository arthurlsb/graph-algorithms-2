from collections import deque

def ordenacaoTopologica(grafo):
    wasVisited = [False] * (grafo.qtdVertices()+1)
    queue = deque([])

    for i in grafo.getVertices():
        if not wasVisited[i]:
            ordenacaoTopologicaSub(grafo, i, wasVisited, queue)

    for index, b in enumerate(queue):
        print(grafo.rotulo(b), end='')
        if index < len(queue) - 1:
            print(' -> ', end='')
    print()

def ordenacaoTopologicaSub(grafo, v, wasVisited, queue):
    wasVisited[v] = True

    for i in grafo.vizinhos(v):
        if not wasVisited[i]:
            ordenacaoTopologicaSub(grafo, i, wasVisited, queue)

    queue.appendleft(v)