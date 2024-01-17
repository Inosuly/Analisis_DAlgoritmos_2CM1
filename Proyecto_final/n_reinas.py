import random
import time

# Contador para almacenar el número de soluciones encontradas
contador = 0
# Lista para representar las columnas y las diagonales ocupadas por las reinas
columna = []
diagonal_izquierda = []
diagonal_derecha = []

# Función recursiva para resolver el problema de las N reinas
def backtrack(fila_actual, n, contador):
    global columna
    global diagonal_izquierda
    global diagonal_derecha

    if fila_actual== n:
        #retorna
        return contador + 1
    
    for x in range(n):
        if columna[x] or diagonal_izquierda[x + fila_actual] or diagonal_derecha[x - fila_actual + n - 1]: 
            continue
        #colocamos una reina
        columna[x] = diagonal_izquierda[x + fila_actual] = diagonal_derecha[x - fila_actual + n - 1] = True
        #enviamos la fila siguiente
        contador = backtrack(fila_actual + 1, n, contador)
        #quitamos la reina para probar otras posibilidades
        columna[x] = diagonal_izquierda[x + fila_actual] = diagonal_derecha[x - fila_actual + n - 1] = False
        
    return contador

def verificar_solucion(tablero):
    for i in range(len(tablero)):
        for j in range(i+1, len(tablero)):
            if tablero[i] == tablero[j] or abs(tablero[i] - tablero[j]) == abs(i - j):
                return False
    return True

# Pruebas aleatorias con medición de tiempo
for _ in range(5):
    n = random.randint(4, 15)
    
    # Reinicializar las variables globales para cada prueba
    columna = [False] * n
    diagonal_izquierda = [False] * (n * 2)
    diagonal_derecha = [False] * (n * 2)
    
    start_time = time.time()
    
    soluciones_encontradas = backtrack(0, n, contador)
    
    end_time = time.time()
    
    tiempo_total = end_time - start_time
    
    print(f'Tamaño del tablero: {n}, Soluciones Encontradas: {soluciones_encontradas}, Tiempo: {tiempo_total:.6f} segundos')
