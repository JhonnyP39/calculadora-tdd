def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("División entre cero")
    return a / b

def raiz(x):
    estimacion = x / 2
    while abs(estimacion**2 - x) > 0.001:
        estimacion = (estimacion + x / estimacion) / 2
    return estimacion

def exponencial(x):
    suma = 1
    termino = 1
    for i in range(1, 20):
        termino = termino * x / i
        suma += termino
    return suma