import random
import heapq
import time

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, from_vertex, to_vertex, weight):
        self.graph[from_vertex][to_vertex] = weight

def generate_random_graph(num_vertices, max_degree, max_weight):
    grafo = Graph()
    for i in range(num_vertices):
        vertex = str(i)
        grafo.add_vertex(vertex)

    for i in range(num_vertices):
        # Generar un grado aleatorio para el vértice actual
        degree = random.randint(1, max_degree)

        # Asegurar que el vértice no se conecte consigo mismo
        neighbors = random.sample(range(num_vertices), min(degree, num_vertices - 1))

        for neighbor in neighbors:
            weight = random.randint(1, max_weight)
            grafo.add_edge(str(i), str(neighbor), weight)

    return grafo

def dijkstra(graph, start_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0

    priority_queue = [(0, start_vertex)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Ejemplo de uso con grafo aleatorio
num_vertices = 5
max_degree = 3
max_weight = 10
grafo_aleatorio = generate_random_graph(num_vertices, max_degree, max_weight)

# Imprimir el grafo generado
print("Grafo Aleatorio:")
for vertex, neighbors in grafo_aleatorio.graph.items():
    print(f"{vertex} -> {neighbors}")

# Aplicar Dijkstra desde un vértice de inicio y medir el tiempo de ejecución
inicio = "0"
start_time = time.time()
resultados_dijkstra = dijkstra(grafo_aleatorio.graph, inicio)
end_time = time.time()

# Imprimir los resultados de Dijkstra
print(f"\nCaminos mínimos desde el vértice {inicio}:")
for vertex, distance in resultados_dijkstra.items():
    print(f"Vértice: {vertex}, Distancia mínima: {distance}")

# Imprimir el tiempo de ejecución
print(f"Tiempo de ejecución: {end_time - start_time} segundos")

