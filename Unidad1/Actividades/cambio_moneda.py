def cambio_moneda(cantidad, denominaciones):
    solucion=[]
    total=0
    denominaciones.sort(reverse=True)
    for denominacion in denominaciones:
        while total + denominacion <= cantidad:
            solucion.append(denominacion)
            total += denominacion
    return solucion
if __name__=='__main__':
    cantidad =153
    denominaciones=[1,2]
    solucion=cambio_moneda(cantidad, denominaciones)
    print("Cambio",solucion)

