import tkinter as tk
import math

def click_boton(valor):
    pantalla.insert(tk.END, valor)

def limpiar():
    pantalla.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(pantalla.get(), {"__builtins__": None}, math.__dict__)
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
    except:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")

# Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora TDD")

pantalla = tk.Entry(ventana, width=30, borderwidth=5)
pantalla.grid(row=0, column=0, columnspan=5)

# Botones básicos
botones = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

fila = 1
columna = 0

for boton in botones:
    if boton == "=":
        tk.Button(ventana, text=boton, width=5, height=2,
                  command=calcular).grid(row=fila, column=columna)
    else:
        tk.Button(ventana, text=boton, width=5, height=2,
                  command=lambda b=boton: click_boton(b)).grid(row=fila, column=columna)
    
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# Botones científicos
tk.Button(ventana, text="√", width=5, height=2,
          command=lambda: click_boton("sqrt(")).grid(row=1, column=4)

tk.Button(ventana, text="sin", width=5, height=2,
          command=lambda: click_boton("sin(")).grid(row=2, column=4)

tk.Button(ventana, text="cos", width=5, height=2,
          command=lambda: click_boton("cos(")).grid(row=3, column=4)

tk.Button(ventana, text="log", width=5, height=2,
          command=lambda: click_boton("log(")).grid(row=4, column=4)

tk.Button(ventana, text="exp", width=5, height=2,
          command=lambda: click_boton("exp(")).grid(row=5, column=4)

# Botón limpiar
tk.Button(ventana, text="C", width=5, height=2,
          command=limpiar).grid(row=5, column=3)

ventana.mainloop()
