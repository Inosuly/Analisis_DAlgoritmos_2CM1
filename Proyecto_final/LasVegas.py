import random
import time

def disponibles(y, n, columna, diagonal_izquierda, diagonal_derecha):
    # Devuelve las columnas no atacadas en la fila y
    disponibles = [x for x in range(n) if not columna[x] and not diagonal_izquierda[x + y] and not diagonal_derecha[x - y + n - 1]]
    return disponibles

def generar_tablero_aleatorio(n):
    # Genera una disposición aleatoria de reinas en un tablero de tamaño n x n
    solucion = []
    columna = [False] * n
    diagonal_izquierda = [False] * (n * 2)
    diagonal_derecha = [False] * (n * 2)

    for y in range(n):
        columnas_disponibles = disponibles(y, n, columna, diagonal_izquierda, diagonal_derecha)
        if columnas_disponibles:
            x = random.choice(columnas_disponibles)
        else:
            break

        columna[x] = diagonal_izquierda[x + y] = diagonal_derecha[x - y + n - 1] = True
        solucion.append((x, y))

    return solucion

# Pruebas aleatorias con medición de tiempo
for i in range(10):
    start_time = time.time()

    n = random.randint(50, 1000)
    solucion_aleatoria = generar_tablero_aleatorio(n)

    end_time = time.time()

    print(f'Tamaño del tablero: {n}, Tiempo: {end_time - start_time:.6f} segundos\n')
