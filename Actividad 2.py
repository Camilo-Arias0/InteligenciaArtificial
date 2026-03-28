import heapq
from collections import defaultdict

# Grafo (red de transporte)
grafo = defaultdict(list)
grafo["A"] = [("B", 5, "L1"), ("D", 10, "L2")]
grafo["B"] = [("C", 7, "L1")]
grafo["D"] = [("C", 3, "L2")]

# Reglas (base de conocimiento)
def evaluar(costo, cambio_linea):
    return costo + (5 if cambio_linea else 0)

# A* simplificado
def buscar(inicio, fin):
    cola = [(0, inicio, None, [])]
    visitados = set()

    while cola:
        costo, nodo, linea, ruta = heapq.heappop(cola)

        if nodo in visitados:
            continue

        ruta = ruta + [nodo]
        visitados.add(nodo)

        if nodo == fin:
            return ruta, costo
