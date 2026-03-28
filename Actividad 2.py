import heapq
from collections import defaultdict

# Grafo (red de transporte)
grafo = defaultdict(list)
grafo["A"] = [("B", 5, "L1"), ("D", 10, "L2")]
grafo["B"] = [("C", 7, "L1")]
grafo["D"] = [("C", 3, "L2")]


