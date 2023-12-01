import random

# Función para calcular la mediana
def calculate_median(arr):
    if not arr:
        return None

    total_sum = sum(arr)
    median = total_sum / len(arr)
    return median

# Función para ordenar la lista usando QuickSort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = calculate_median(arr)

    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + equal + quick_sort(right)

# Función para ordenar la lista usando Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Función para la búsqueda binaria
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Si el elemento no se encuentra en la lista
def print_colored_list(arr, color, target):
    # Define códigos de escape ANSI para colores de texto
    colors = {
        'green': '\033[32m',
        'blue': '\033[34m',
        'purple': '\033[35m',
        'reset': '\033[0m',
        'highlight': '\033[1;37;41m'  # Fondo rojo para resaltar
    }

    # Imprime la lista con el color especificado y resalta el número si se encuentra en la lista
    for num in arr:
        if num == target:
            print(colors['highlight'] + str(num) + colors['reset'], end=' ')
        else:
            print(colors[color] + str(num) + colors['reset'], end=' ')

# Pedir al usuario que ingrese el tamaño de la lista
try:
    size = int(input("Ingrese el tamaño de la lista: "))
except ValueError:
    print("Entrada no válida. Debe ser un número entero.")
    exit()
    
# Generar la lista con números aleatorios
lista = [random.randint(1, 100) for _ in range(size)]

print("Lista original:", end=' ')
print_colored_list(lista, 'green', target)

while True:
    # Pedir al usuario que elija si desea ordenar la lista
    print("¿Desea ordenar la lista?")
    print("1. Sí")
    print("2. No")

    try:
        sort_choice = int(input("Ingrese el número correspondiente a su elección: "))
    except ValueError:
        print("Entrada no válida. Debe ser un número.")
        continue

    if sort_choice == 1:
        # Pedir al usuario que elija el método de ordenación
        print("Seleccione el método de ordenación:")
        print("1. QuickSort")
        print("2. Bubble Sort")

        try:
            method_choice = int(input("Ingrese el número correspondiente al método: "))
        except ValueError:
            print("Entrada no válida. Debe ser un número.")
            continue

        # Ordenar la lista según el método elegido
        if method_choice == 1:
            lista_ordenada = quick_sort(lista.copy())  # Usar una copia para no modificar la original
            method_name = "QuickSort"
            print(f"Lista ordenada usando {method_name}: ", end='')
            print_colored_list(lista_ordenada, 'blue', target)
        elif method_choice == 2:
            lista_ordenada = list(lista)  # Copia la lista para no modificar la original
            bubble_sort(lista_ordenada)
            method_name = "Bubble Sort"
            print(f"Lista ordenada usando {method_name}: ", end='')
            print_colored_list(lista_ordenada, 'purple', target)
        else:
            print("Opción no válida. Se usará QuickSort por defecto.")
            lista_ordenada = quick_sort(lista.copy())  # Usar una copia para no modificar la original
            method_name = "QuickSort"
    elif sort_choice == 2:
        lista_ordenada = list(lista)  # Usar una copia de la lista no ordenada
        method_name = "Ningún método (lista no ordenada)"
    else:
        print("Opción no válida. Por favor, seleccione 1 o 2.")
        continue

    # Mostrar la lista ordenada
    print(f"Lista ordenada usando {method_name}: {lista_ordenada}")
# Inicializar la variable target
    target = None
    while True:
        # Pedir al usuario que elija si desea buscar un número
        print("¿Desea buscar un número en la lista?")
        print("1. Sí")
        print("2. No")

        try:
            search_choice = int(input("Ingrese el número correspondiente a su elección: "))
        except ValueError:
            print("Entrada no válida. Debe ser un número.")
            continue

        if search_choice == 1:
            # Pedir al usuario que ingrese el número a buscar
            try:
                target = int(input("Ingrese el número que desea buscar: "))
            except ValueError:
                print("Entrada no válida. Debe ser un número.")
                continue

            # Realizar la búsqueda según el método elegido
            if method_choice == 1:
                if target in lista_ordenada:
                    print(f"El elemento {target} se encuentra en la lista ordenada.")
                    print(f"Lista ordenada usando {method_name}: ", end='')
                    print_colored_list(lista_ordenada, 'blue', target)
                else:
                    print(f"El elemento {target} no se encuentra en la lista.")
            elif method_choice == 2:
                if target in lista_ordenada:
                    print(f"El elemento {target} se encuentra en la lista ordenada.")
                    print(f"Lista ordenada usando {method_name}: ", end='')
                    print_colored_list(lista_ordenada, 'purple', target)
                else:
                    print(f"El elemento {target} no se encuentra en la lista.")
            else:
                print("Opción no válida. Se usará QuickSort por defecto.")
                if target in lista_ordenada:
                    print(f"El elemento {target} se encuentra en la lista ordenada.")
                    print(f"Lista ordenada usando {method_name}: ", end='')
                    print_colored_list(lista_ordenada, 'blue', target)
                else:
                    print(f"El elemento {target} no se encuentra en la lista.")
        elif search_choice == 2:
            break  # Salir del bucle si el usuario no desea buscar más números
        else:
            print("Opción no válida. Por favor, seleccione 1 o 2.")
            continue

    # Preguntar si el usuario quiere ordenar y buscar nuevamente
    print("¿Desea ordenar y buscar más números?")
    print("1. Sí")
    print("2. No")

    try:
        repeat_choice = int(input("Ingrese el número correspondiente a su elección: "))
    except ValueError:
        print("Entrada no válida. Debe ser un número.")
        break

    if repeat_choice == 2:
        break  # Salir del bucle principal si el usuario no desea repetir el proceso

print("Programa finalizado.")
