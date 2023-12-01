import random
import time
import matplotlib.pyplot as plt

def calculate_median(arr):
    if not arr:
        return None

    # Calcula la media de los elementos
    total_sum = sum(arr)
    median = total_sum / len(arr)
    return median

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Elegir el pivote como la media 
    pivot = calculate_median(arr)

    # Particionar la lista
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Aplicar recursivamente en sublistas izquierda y derecha
    return quick_sort(left) + equal + quick_sort(right)
execution_tiempos =[]
sizes=[]
for i in range(1, 101):
    #generar tamaños aletorios 
    size = random.randint(600, 10000)
    print(i, ".-", size)
    # Generar la lista con números aleatorios
    lista = [random.randint(1, 100) for _ in range(size)]
    #print("Lista original:", lista)
# Llamar a QuickSort
    start_time= time.time()
    lista_ordenada = quick_sort(lista)
    #print("Lista ordenada:", lista_ordenada) # Color verde brillante
    end_time= time.time()
    execution_time= end_time - start_time
    execution_tiempos.append(execution_time)
    sizes.append(size)
print(execution_tiempos)
print(sizes)
#Graficar el tiempo de ejecucion 
plt.plot(sizes,  execution_tiempos, 'ro')
plt.show()

