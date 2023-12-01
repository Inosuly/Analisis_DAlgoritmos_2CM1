import heapq #libreria para manejar arboles
from collections import Counter #libreria para contar frecuencia

class Nodo:
    #Constructor
    def __init__(self, simbolo, frecuencia):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha= None
#Sobrecragar del metodo para comparar objetos
    def __lt__(self, otro):
        return self.frecuencia<otro.frecuencia        

#construir el arbol
def construir_arbol(frecuencia):
    heap =[Nodo(simbolo, frecuencia) for simbolo, frecuencia in frecuencia.items()]
    #crear el arbol
    heapq.heapify(heap)

    #crear los nodo con la suma de la frecuencia
    while len(heap)>1:
        nodo_izq=heapq.heappop(heap)
        nodo_der=heapq.heappop(heap)

        nodo_padre=Nodo(None, nodo_izq.frecuencia + nodo_der.frecuencia)
        nodo_padre.izquierda = nodo_izq
        nodo_padre.derecha = nodo_der
        #agregar nodo padre al arbol
        heapq.heappush(heap, nodo_padre)
    return heapq[0]

def  generar_codigos(arbol, codigo_actual="", dict_frecuencias =None):
    if dict_frecuencias is None:
        #Diccionario vacio
        dict_frecuencias={}
    #verificar si el nodo actual es una hoja, asignar el codigo al simbolo
    if arbol.simbolo is not None:
        dict_frecuencias[arbol.simbolo]= codigo_actual
    #generar recursivamente los codigos
    if arbol.izquierda is not None:
        generar_codigos(arbol.izquierda, codigo_actual+0, dict_frecuencias)
    if arbol.derecha is not None:
        generar_codigos(arbol.derecha, codigo_actual+ 1, dict_frecuencias)
    return dict_frecuencias


def codificar(texto, dict_frecuencias):
    return ''.join(dict_frecuencias[simbolo] for simbolo in texto)

#############################################################
if __name__== '__main__':
    texto ='palabra'
    #diccionario de frecuencia
    frecuencias = Counter(texto)
    print(frecuencias)
    arbol = construir_arbol(frecuencias)
    codigos= generar_codigos(arbol)
    print(codigos)
    texto_codificado = codificar(texto, codigos)
    print(texto_codificado)