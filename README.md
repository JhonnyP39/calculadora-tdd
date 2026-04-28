# 🧮 Calculadora con TDD

## 📌 Descripción del proyecto

Este proyecto consiste en el desarrollo de una calculadora básica utilizando Python, aplicando la metodología **TDD (Test Driven Development)**.

La aplicación permite realizar operaciones matemáticas fundamentales como suma, resta, multiplicación y división, así como funciones científicas como raíz cuadrada, seno, coseno, logaritmo y exponencial, garantizando su correcto funcionamiento mediante pruebas unitarias.

---

## 🎯 Objetivo

Desarrollar una calculadora funcional aplicando TDD, asegurando la calidad del código mediante la creación y ejecución de pruebas automatizadas.

---

## 🧪 Metodología TDD

Se utilizó el ciclo de desarrollo TDD:

1. **Red**: Se crean pruebas que inicialmente fallan.
2. **Green**: Se implementa el código necesario para que las pruebas pasen.
3. **Refactor**: Se mejora el código sin afectar las pruebas.

---

## 📂 Estructura del proyecto

```
calculadora-tdd/
│
├── calculadora.py       # Lógica de operaciones
├── test_calculadora.py  # Pruebas unitarias
├── main.py              # Interfaz gráfica (Tkinter)
└── README.md            # Documentación
```

---

## ⚙️ Requisitos

* Python 3.x
* pytest

Instalación de pytest:

```bash
pip install pytest
```

---

## ▶️ Ejecución del programa

Para ejecutar la calculadora:

```bash
python main.py
```

---

## ✅ Ejecución de pruebas

Para ejecutar las pruebas unitarias:

```bash
pytest
```

---

## 🧠 Funcionalidades

* Suma de números
* Resta de números
* Multiplicación
* División (con validación de división entre cero)
* Raíz cuadrada
* Funciones trigonométricas (sin, cos)
* Logaritmo
* Función exponencial

---

## ⚠️ Manejo de errores

El sistema incluye validaciones para evitar errores como la división entre cero o expresiones inválidas, mostrando mensajes adecuados al usuario.

---

## 👨‍💻 Autor

Yoni Perez

---

## 📅 Fecha

27 Abril 2026
