# Sistema de Gestion de Garaje

## Descripcion

Aplicacion de escritorio con interfaz grafica (Tkinter) para registrar
y visualizar vehiculos en un garaje. Desarrollada con arquitectura modular
en Python aplicando Programacion Orientada a Objetos.

---

## Estructura del Proyecto

garaje_app/
├── main.py                      <- Punto de entrada
├── modelos/
│   ├── __init__.py
│   └── vehiculo.py              <- Clase Vehiculo (POO)
├── servicios/
│   ├── __init__.py
│   └── garaje_servicio.py       <- Logica del sistema
└── ui/
    ├── __init__.py
    └── app_tkinter.py           <- Interfaz grafica Tkinter

---

## Requisitos

- Python 3.x
- Tkinter (ya incluido con Python, no requiere instalacion adicional)

---

## Como Ejecutar

python main.py

---

## Funcionalidades

- Registrar vehiculos con placa, marca y propietario
- Visualizar vehiculos registrados en una tabla
- Validacion de campos vacios
- Validacion de placas duplicadas
- Limpiar formulario con un clic
- Contador de vehiculos registrados