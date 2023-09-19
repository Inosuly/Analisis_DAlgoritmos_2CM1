def fib(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fib(n-1) + fib(n-2)
def fact(n):
   if n==0 or n==1:
            resultado=1
   elif n>1:
            resultado=n*fact(n-1)
   return resultado
try:
    n = int(input("Introduce un numero "))
except ValueError:
    print("Entrada no válida. Debe ser un número entero.")
    exit()
print("\nFactorial: ", fact(n))
print("Numero Fibonacci:", fib(n))  
print("sucesión de Fibonacci hasta la posicion", n)
for x in range(n):
    print(fib(x))




