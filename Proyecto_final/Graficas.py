import random
import time
import matplotlib.pyplot as plt

# Función recursiva para resolver el problema de las N reinas con poda por factibilidad
def backtrack(fila_actual, n, columna, diagonal_izquierda, diagonal_derecha):
    contador = 0

    if fila_actual == n:
        # Retorna
        return contador + 1

    for x in range(n):
        # Verificamos si la posición es factible antes de colocar una reina
        if columna[x] or diagonal_izquierda[x + fila_actual] or diagonal_derecha[x - fila_actual + n - 1]:
            continue

        # Colocamos una reina
        columna[x] = diagonal_izquierda[x + fila_actual] = diagonal_derecha[x - fila_actual + n - 1] = True

        # Enviamos la fila siguiente
        contador = backtrack(fila_actual + 1, n, columna, diagonal_izquierda, diagonal_derecha)

        # Quitamos la reina para probar otras posibilidades (backtracking)
        columna[x] = diagonal_izquierda[x + fila_actual] = diagonal_derecha[x - fila_actual + n - 1] = False

    return contador

# La Vegas
def disponibles(y, n, columna, diagonal_izquierda, diagonal_derecha):
    # Devuelve las columnas no atacadas en la fila y
    disponibles = [x for x in range(n) if not columna[x] and not diagonal_izquierda[x + y] and not diagonal_derecha[x - y + n - 1]]
    return disponibles

def soluciones_encontradas_las_vegas(n, columna, diagonal_izquierda, diagonal_derecha):
    columna = [False] * n
    diagonal_izquierda = [False] * (n * 2)
    diagonal_derecha = [False] * (n * 2)

    # Generar un tablero aleatorio y verificar su solución
    tablero_random = generar_tablero_aleatorio(n)
    start_time_verificar_solucion = time.time()
    solucion_valida = verificar_solucion([pos[0] for pos in tablero_random])
    end_time_verificar_solucion = time.time()

    return {
        'size': n,
        'verificar_solucion_time': end_time_verificar_solucion - start_time_verificar_solucion,
        'verificar_solucion_valid': solucion_valida
    }

def verificar_solucion(tablero):
    for i in range(len(tablero)):
        for j in range(i + 1, len(tablero)):
            if tablero[i] == tablero[j] or abs(tablero[i] - tablero[j]) == abs(i - j):
                return False
    return True

def generar_tablero_aleatorio(n):
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

def realizar_pruebas_aleatorias(i):
    resultados_backtrack = []
    resultados_las_vegas = []

    for _ in range(i):
        n_backtrack = random.randint(4, 10)  # Tamaños pequeños para Backtracking
        n_las_vegas = random.randint(50, 100)  # Tamaños más grandes para La Vegas

        # Realizar pruebas de Backtracking
        columna_backtrack = [False] * n_backtrack
        diagonal_izquierda_backtrack = [False] * (n_backtrack * 2)
        diagonal_derecha_backtrack = [False] * (n_backtrack * 2)
        start_time_backtrack = time.time()
        soluciones_encontradas_backtrack = backtrack(0, n_backtrack, columna_backtrack, diagonal_izquierda_backtrack, diagonal_derecha_backtrack)
        end_time_backtrack = time.time()

        resultados_backtrack.append({
            'size': n_backtrack,
            'backtrack_time': end_time_backtrack - start_time_backtrack,
            'backtrack_solutions': soluciones_encontradas_backtrack
        })

        # Realizar pruebas de La Vegas
        columna_las_vegas = [False] * n_las_vegas
        diagonal_izquierda_las_vegas = [False] * (n_las_vegas * 2)
        diagonal_derecha_las_vegas = [False] * (n_las_vegas * 2)
        start_time_las_vegas = time.time()
        resultado_las_vegas = soluciones_encontradas_las_vegas(n_las_vegas, columna_las_vegas, diagonal_izquierda_las_vegas, diagonal_derecha_las_vegas)
        end_time_las_vegas = time.time()

        resultado_las_vegas['verificar_solucion_time'] = end_time_las_vegas - start_time_las_vegas
        resultados_las_vegas.append(resultado_las_vegas)

    return resultados_backtrack, resultados_las_vegas

def graficar_tiempos(resultados_backtrack, resultados_las_vegas):
    tamanos_backtrack = [resultado['size'] for resultado in resultados_backtrack]
    tiempos_backtrack = [resultado['backtrack_time'] for resultado in resultados_backtrack]
    tiempos_las_vegas = [resultado['verificar_solucion_time'] for resultado in resultados_las_vegas]

    plt.figure(figsize=(10, 6))
    plt.plot(tamanos_backtrack, tiempos_backtrack, label='Backtracking')
    plt.plot(tamanos_backtrack, tiempos_las_vegas, label='La Vegas')
    plt.xlabel('Tamaño del Tablero (N)')
    plt.ylabel('Tiempo de Ejecución (segundos)')
    plt.title('Comparación de Tiempos de Ejecución')
    plt.legend()
    plt.show()

# Realizar pruebas aleatorias
resultados_backtrack, resultados_las_vegas = realizar_pruebas_aleatorias(20)

# Graficar tiempos de ejecución
graficar_tiempos(resultados_backtrack, resultados_las_vegas)

