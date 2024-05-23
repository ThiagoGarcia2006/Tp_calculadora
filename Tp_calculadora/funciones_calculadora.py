

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."
    
def multiplicar(a, b):
    return a * b

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)    