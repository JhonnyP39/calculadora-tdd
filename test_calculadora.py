<<<<<<< HEAD
from calculadora import *

def test_suma():
    assert suma(2, 3) == 5

def test_resta():
    assert resta(5, 3) == 2

def test_multiplicacion():
    assert multiplicacion(2, 3) == 6

def test_division():
    assert division(6, 3) == 2

def test_raiz():
    assert abs(raiz(9) - 3) < 0.001

def test_exponencial():
    assert abs(exponencial(1) - 2.718) < 0.001
=======
from calculadora import *

def test_suma():
    assert suma(2, 3) == 5

def test_resta():
    assert resta(5, 3) == 2

def test_multiplicacion():
    assert multiplicacion(2, 3) == 6

def test_division():
    assert division(6, 3) == 2

def test_raiz():
    assert abs(raiz(9) - 3) < 0.001

def test_exponencial():
    assert abs(exponencial(1) - 2.718) < 0.001
    # pruebas creadas
>>>>>>> 3b823086489d58905058e4707491cfce270630b1
