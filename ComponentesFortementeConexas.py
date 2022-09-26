from collections import deque

def ComponentesFortementeConexas(graph):
    stack = deque([])
    qttVertexes = graph.qtdVertices()
    wasVisited = [False] * (qttVertexes + 1)
    wasDesigned = [False] * (qttVertexes + 1)
    classes = [[] for i in range(qttVertexes + 1)]
    revereseGraph = graph.getGrafoTransposto()

    for index, vertex in enumerate(graph.vertices.keys()):
        dfs(graph, vertex, wasVisited, stack)

    for vertex in stack:
        attribute(revereseGraph, vertex, vertex, wasDesigned, classes)

    printComponentesFortementeConexas(classes)
    return classes

def dfs(graph, vertex, wasVisited, stack):
    if not wasVisited[vertex]:
        wasVisited[vertex] = True
        neighbors = graph.vizinhos(vertex).keys()
        for neighbor in neighbors:
            dfs(graph, neighbor, wasVisited, stack)
        stack.appendleft(vertex)

def attribute(revereseGraph, vertex, raiz, wasDesigned, classes):
    if not wasDesigned[vertex]:
        classes[raiz].append(vertex)
        wasDesigned[vertex] = True
        neighbors = revereseGraph.vizinhos(vertex).keys()
        for neighbor in neighbors:
            attribute(revereseGraph, neighbor, raiz, wasDesigned, classes)

def printComponentesFortementeConexas(classes):
    for classe in classes:
        if len(classe) > 0:
            classList = []
            for index, vertex in enumerate(classe):
                classList.append(vertex)
            print(str(classList)[1:-1])