# Punto de entrada de la aplicacion.
# Crea la ventana principal de Tkinter y lanza la interfaz grafica del sistema de garaje.

import tkinter as tk
from ui.app_tkinter import AppTkinter


def main():
    """
    Funcion principal: crea la ventana raiz de Tkinter
    y lanza la aplicacion de gestion de garaje.
    """
    # Crear la ventana principal de Tkinter
    root = tk.Tk()

    # Crear la aplicacion pasandole la ventana raiz
    app = AppTkinter(root)

    # Iniciar el bucle principal de la interfaz
    app.iniciar()


# Ejecutar solo si se corre este archivo directamente
if __name__ == "__main__":
    main()