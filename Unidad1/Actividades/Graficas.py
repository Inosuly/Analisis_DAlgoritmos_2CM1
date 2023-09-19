import matplotlib.pyplot as plt
import numpy as np
import math 
# factorial 
def f3(x): 
    if(x==0):
        return 1
    else:
        return (x * f3(x-1))
x = np.linspace(0, 10, 100)

fig, ax = plt.subplots()  # Crea la figura y los ejes.
#funciones para graficar 
ax.plot(x, x*0.1, label='O(n)')   #Lineal 
ax.plot(x, np.exp(x)*0.0002, label='O(2^n)')#expondecial 
ax.plot(x, x**2, label='O(n²)') #cuadratica 
ax.plot(x, np.log(x), label='O(log n)') #logarítmica
ax.plot(f3, label='O(n!)') #factorial 


#-------------
ax.set_xlabel('Tiempo')
ax.set_ylabel('Amplitud')
ax.set_title("Ejemplo Python")  
ax.legend()  # Imprime la leyenda.
plt.grid(True)
plt.show() # para que se muestre.