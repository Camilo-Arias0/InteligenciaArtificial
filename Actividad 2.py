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
         for destino, tiempo, nueva_linea in grafo[nodo]:
            cambio = linea and linea != nueva_linea
            nuevo_costo = evaluar(costo + tiempo, cambio)
            heapq.heappush(cola, (nuevo_costo, destino, nueva_linea, ruta))

            return None, float("inf")

    # Ejecución
    ruta, costo = buscar("A", "C")
    print("Ruta:", ruta)
    print("Costo:", costo)

    #  Pruebas 
    def test_ruta_correcta():
    ruta, _ = buscar("A", "C")
    assert ruta in [["A", "B", "C"], ["A", "D", "C"]]
    print("✔️ Test ruta válida OK")

def test_costo_minimo():
    _, costo = buscar("A", "C")
    assert costo <= 15  # ruta óptima esperada
    print("✔️ Test costo mínimo OK")

def test_sin_ruta():
    ruta, costo = buscar("C", "A")
    assert ruta is None
    assert costo == float("inf")
    print("✔️ Test sin ruta OK")

def test_mismo_origen_destino():
    ruta, costo = buscar("A", "A")
    assert ruta == ["A"]
    assert costo == 0
    print("✔️ Test mismo nodo OK")

if _name_ == "_main_":
    test_ruta_correcta()
    test_costo_minimo()
    test_sin_ruta()
    test_mismo_origen_destino()
