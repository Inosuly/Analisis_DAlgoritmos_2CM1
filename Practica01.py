#Giovanna Inosuli Campos Flores#
#2020670125             grupo: 3CM1
#Este programa  utiliza el metodo ordenamiento de burbuja y Burbuja optimizada

import time

def ord_burbuja(arreglo):
    
    n = len(arreglo)
    for i in range(n-1):      
        
        for j in range(n-1-i): 
           
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]

def burbuja_optimus(arreglo):
    n = len(arreglo)
  
    for i in range(n-1):
        intercambio = False
 
        for j in range(n-1-i):
            if arreglo[j] > arreglo[j+1] :
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
                intercambio = True
 
        if intercambio == False:
            break
inicio = time.time()
try:
    size = int(input("Introduce el tamaño de la lista: "))
except ValueError:
    print("Entrada no válida. Debe ser un número entero.")
    exit()

# Pedir al usuario los elementos de la lista
try:
    lista = [float(input(f"Introduce el elemento {i+1}: ")) for i in range(size)]
except ValueError:
    print("Entrada no válida. Debe ser un número.")
    exit()

print(""" ordenar comno 
    1) Metodo Burbuja                    2)Metodo Burbuja optimizada""")
opcion = input ('Seleciona  ')
print("\nLista")    

if opcion  == "1":
    print("Burbuja\n")
    inicio = inicio
    print("Lista")
    print(lista)
    ord_burbuja(lista)
    tiempo_transcurrido = time.time() - inicio
    print("\nLista Ordenada")
    print(lista)
    tiempo_transcurrido
    print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")

elif opcion  == "2":
        inicio = inicio
        print("Burbuja Optimizada")

        print("Lista\n", lista)
        burbuja_optimus(lista)
        tiempo_transcurrido = time.time() - inicio
        print("\nLista Ordenada")
        print(lista, "\n")
        tiempo_transcurrido
        print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")
else:
        print("Opcion no valida")
