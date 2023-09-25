def fact(n):
    if n <= 1: #es caso base n= 1, su factorial seria 1
        return n
    else:
        return n * fact(n-1)
def fib(n):
    if n<=1: #caso base f(1)=1
        return 1
    elif n==0:
        return 0 #caso base f(0)=0
    else: 
        return fib(n-1) + fib(n-2) # caso genral 
    
x= int(input("ingresa un numero  "))
print("factorial", fact(x))
print("fibigonaci", fib(x))


  