import tkinter as tk
import calculadora as calc

ventana = tk.Tk()
ventana.title("Calculadora TDD")

pantalla = tk.Entry(ventana, font=("Arial", 18))
pantalla.pack()

def calcular():
    try:
        resultado = eval(pantalla.get())
        pantalla.delete(0, tk.END)
        pantalla.insert(0, resultado)
    except:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")

tk.Button(ventana, text="Calcular", command=calcular).pack()

ventana.mainloop()