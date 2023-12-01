import random
import heapq
import time
class Graph:
    def __init__(self): #constructor
        # Utilizamos un diccionario
        #para almacenar los vértices y las aristas con pesos
        self.graph = {}

    def add_vertex(self, vertex):
        # Agrega un vértice al grafo si no existe
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, inicio, final, peso):
        # Agrega una arista con peso entre los vértices dados
        if inicio in self.graph and final not in self.graph[inicio]:
            self.graph[inicio].append((final, peso))
        else:
            print(f"Error")

def dijkstra(graph, inicio):
    # Inicializar el diccionario de distancias mínimas
    distancias= {vertex: float('infinity') for vertex in graph}
    distancias[inicio] = 0

    # Usar un heap para manejar las prioridades de los vértices
    cola_prioridad= [(0, inicio)]

    while cola_prioridad:
        distancia_actual, vertice_actual= heapq.heappop(cola_prioridad)

        # Si la distancia actual es mayor que la registrada, continuar al siguiente vértice
        if distancia_actual > distancias[vertice_actual]:
            continue

        # Actualizar las distancias para los vértices adyacentes
        for vecino, peso in graph[vertice_actual]:
            distancia = distancia_actual + peso

            # Si se encuentra un camino más corto, actualizar la distancia
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(cola_prioridad, (distancia, vecino))

    return distancias
#funcion para medir tiempo
def medir_tiempo(funcion, *args, **kwargs):
    inicio_tiempo = time.time()
    resultado = funcion(*args, **kwargs)
    fin_tiempo = time.time()
    tiempo_ejecucion = fin_tiempo - inicio_tiempo
    print(f'Tiempo de ejecución: {tiempo_ejecucion} segundos')
    return resultado

# Ejemplo de uso:
grafo = Graph()# Crear un Grafo
# Agregar vértices
num_vertices = 10000  #asignamos el numero de vertices deseados
aristas=1000    #asignamos el numero de aristas deseados
for i in range(num_vertices+1):
    grafo.add_vertex(str(i))
# Agregar aristas con pesos aleatorios
for _ in range(aristas):  
    inicio= str(random.randint(0, num_vertices - 1))
    final = str(random.randint(0, num_vertices - 1))
    peso = random.randint(1, 100)
    grafo.add_edge(inicio, final, peso)

# Mostrar grafo
#print(grafo.graph)

# Calcular los caminos mínimos desde el vértice '0' (por ejemplo)
resultados = dijkstra(grafo.graph, '0')

# Mostrar los resultados de Dijkstra
for vertex, distancia in resultados.items():
    print(f'Distancia mínima desde 0 hasta {vertex}: {distancia}')

# Calcular los caminos mínimos desde el vértice '0' y medir el tiempo de ejecución
medir_tiempo(dijkstra, grafo.graph, '0')