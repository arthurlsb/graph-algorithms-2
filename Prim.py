def prim(grafo):
    inicialVertex = 1
    qttVertexes = grafo.qtdVertices()
    wasVisited = [False] * (qttVertexes + 1)
    keys = [999999999] * (qttVertexes + 1)
    predecessors = [None] * (qttVertexes + 1)
    keys[inicialVertex] = 0
    queue = [0] + list(grafo.vertices.keys())

    while len(queue) != 1:
        keysNonVisiteds = [keys[i] for i in queue]
        minorKey = min(keysNonVisiteds)
        indexMinorKey = keysNonVisiteds.index(minorKey)
        minorVertex = queue.pop(indexMinorKey)
        wasVisited[minorVertex] = True

        for neighbor in grafo.vizinhos(minorVertex):
            pesoAresta = grafo.peso(minorVertex, neighbor)
            if neighbor in queue and pesoAresta < keys[neighbor]:
                predecessors[neighbor] = minorVertex
                keys[neighbor] = pesoAresta

    printPrim(predecessors, keys)
    return predecessors, keys

def printPrim(predecessors, keys):
    edges = []
    total = 0
    
    for chave in keys:
        if chave < 999999999:
            total += chave
    print(total)
    
    for index, v in enumerate(predecessors):
        if v is not None:
            edges.append(', {}-{}'.format(index, v))
    
    frmArestas = ''
    
    for aresta in edges:
        frmArestas += str(aresta)
    
    print(frmArestas[2:])