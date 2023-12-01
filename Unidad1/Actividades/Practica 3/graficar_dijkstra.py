import random
import heapq
import time
import matplotlib.pyplot as plt
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

def generar_grafo_aleatorio(num_vertices):
    grafo = Graph()

    for i in range(num_vertices):
        grafo.add_vertex(str(i))

    for _ in range(num_vertices * 2):
        inicio = str(random.randint(0, num_vertices - 1))
        final = str(random.randint(0, num_vertices - 1))
        peso = random.randint(1, 100)
        grafo.add_edge(inicio, final, peso)

    return grafo.graph

def realizar_pruebas(num_pruebas, tamanios_grafos):
    resultados = []

    for num_vertices in tamanios_grafos:
        tiempos_ejecucion = []

        for _ in range(num_pruebas):
            grafo = generar_grafo_aleatorio(num_vertices)
            inicio_tiempo = time.time()
            dijkstra(grafo, '0')  # Suponiendo que siempre iniciamos desde el vértice '0'
            fin_tiempo = time.time()
            tiempo_ejecucion = fin_tiempo - inicio_tiempo
            tiempos_ejecucion.append(tiempo_ejecucion)

        resultados.append((num_vertices, sum(tiempos_ejecucion) / num_pruebas))

    return resultados

def graficar_tiempos(resultados):
    tamanios_grafos, tiempos_promedio = zip(*resultados)
    plt.plot(tamanios_grafos, tiempos_promedio, marker='o')
    plt.title('Tiempo de ejecución de Dijkstra ')
    plt.xlabel('Número de vértices')
    plt.ylabel('Tiempo de ejecución promedio (segundos)')
    plt.show()

# Ejemplo de uso
num_pruebas = 10
tamanios_grafos = [10000, 20000, 30000, 40000, 50000]  # Puedes ajustar esto según tus necesidades

resultados = realizar_pruebas(num_pruebas, tamanios_grafos)
graficar_tiempos(resultados)