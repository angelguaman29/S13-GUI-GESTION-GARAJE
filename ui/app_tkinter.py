# Interfaz grafica del sistema de garaje desarrollada con Tkinter.
# Conecta la UI con la logica del servicio.


import tkinter as tk
from tkinter import ttk, messagebox
from servicios.garaje_servicio import GarajeServicio


class AppTkinter:
    """
    Clase que construye y gestiona la ventana principal
    de la aplicacion usando Tkinter.

    Componentes de la interfaz:
        - Campos de texto: placa, marca, propietario.
        - Boton Agregar vehiculo.
        - Boton Limpiar campos.
        - Tabla (Treeview) para mostrar los vehiculos registrados.
        - Etiqueta de total de vehiculos.
    """

    def __init__(self, root):
        """
        Constructor: recibe la ventana raiz de Tkinter
        y construye todos los componentes de la interfaz.

        Parametros:
            root (tk.Tk) : Ventana principal de la aplicacion.
        """
        # Ventana principal
        self.root = root
        self.root.title("Sistema de Gestion de Garaje")
        self.root.geometry("700x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        # Instancia del servicio (logica del sistema)
        self.servicio = GarajeServicio()

        # Construir los componentes de la interfaz
        self._construir_titulo()
        self._construir_formulario()
        self._construir_botones()
        self._construir_tabla()
        self._construir_pie()

    # --------------------------------------------------------
    # METODOS DE CONSTRUCCION DE LA INTERFAZ
    # --------------------------------------------------------

    def _construir_titulo(self):
        """Crea el titulo principal de la ventana."""
        frame_titulo = tk.Frame(self.root, bg="#2c3e50", pady=12)
        frame_titulo.pack(fill="x")

        tk.Label(
            frame_titulo,
            text="SISTEMA DE GESTION DE GARAJE",
            font=("Arial", 16, "bold"),
            fg="white",
            bg="#2c3e50"
        ).pack()

    def _construir_formulario(self):
        """Crea el formulario de entrada de datos del vehiculo."""
        frame_form = tk.LabelFrame(
            self.root,
            text="Datos del Vehiculo",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0",
            padx=15,
            pady=10
        )
        frame_form.pack(fill="x", padx=20, pady=10)

        # --- Placa ---
        tk.Label(
            frame_form, text="Placa:",
            font=("Arial", 10), bg="#f0f0f0", width=12, anchor="e"
        ).grid(row=0, column=0, padx=5, pady=5)

        self.entry_placa = tk.Entry(frame_form, font=("Arial", 10), width=25)
        self.entry_placa.grid(row=0, column=1, padx=5, pady=5)

        # --- Marca ---
        tk.Label(
            frame_form, text="Marca:",
            font=("Arial", 10), bg="#f0f0f0", width=12, anchor="e"
        ).grid(row=1, column=0, padx=5, pady=5)

        self.entry_marca = tk.Entry(frame_form, font=("Arial", 10), width=25)
        self.entry_marca.grid(row=1, column=1, padx=5, pady=5)

        # --- Propietario ---
        tk.Label(
            frame_form, text="Propietario:",
            font=("Arial", 10), bg="#f0f0f0", width=12, anchor="e"
        ).grid(row=2, column=0, padx=5, pady=5)

        self.entry_propietario = tk.Entry(frame_form, font=("Arial", 10), width=25)
        self.entry_propietario.grid(row=2, column=1, padx=5, pady=5)

    def _construir_botones(self):
        """Crea los botones Agregar y Limpiar."""
        frame_botones = tk.Frame(self.root, bg="#f0f0f0")
        frame_botones.pack(pady=5)

        # Boton Agregar
        tk.Button(
            frame_botones,
            text="  Agregar Vehiculo  ",
            font=("Arial", 10, "bold"),
            bg="#27ae60",
            fg="white",
            activebackground="#2ecc71",
            cursor="hand2",
            command=self._agregar_vehiculo
        ).grid(row=0, column=0, padx=10)

        # Boton Limpiar
        tk.Button(
            frame_botones,
            text="  Limpiar Campos  ",
            font=("Arial", 10, "bold"),
            bg="#e74c3c",
            fg="white",
            activebackground="#c0392b",
            cursor="hand2",
            command=self._limpiar_campos
        ).grid(row=0, column=1, padx=10)

    def _construir_tabla(self):
        """Crea la tabla donde se muestran los vehiculos registrados."""
        frame_tabla = tk.LabelFrame(
            self.root,
            text="Vehiculos Registrados",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0",
            padx=10,
            pady=5
        )
        frame_tabla.pack(fill="both", expand=True, padx=20, pady=5)

        columnas = ("placa", "marca", "propietario")

        self.tabla = ttk.Treeview(
            frame_tabla,
            columns=columnas,
            show="headings",
            height=8
        )

        # Encabezados
        self.tabla.heading("placa",       text="Placa")
        self.tabla.heading("marca",       text="Marca")
        self.tabla.heading("propietario", text="Propietario")

        # Ancho de columnas
        self.tabla.column("placa",       width=150, anchor="center")
        self.tabla.column("marca",       width=200, anchor="center")
        self.tabla.column("propietario", width=280, anchor="center")

        # Scrollbar
        scrollbar = ttk.Scrollbar(
            frame_tabla,
            orient="vertical",
            command=self.tabla.yview
        )
        self.tabla.configure(yscrollcommand=scrollbar.set)

        self.tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def _construir_pie(self):
        """Crea la etiqueta del total de vehiculos."""
        self.label_total = tk.Label(
            self.root,
            text="Total de vehiculos registrados: 0",
            font=("Arial", 9),
            bg="#f0f0f0",
            fg="#555555"
        )
        self.label_total.pack(pady=5)

    # --------------------------------------------------------
    # EVENTOS DE BOTONES
    # --------------------------------------------------------

    def _agregar_vehiculo(self):
        """
        Evento del boton Agregar.
        Lee los campos, llama al servicio y actualiza la tabla.
        """
        placa       = self.entry_placa.get()
        marca       = self.entry_marca.get()
        propietario = self.entry_propietario.get()

        # Llamar al servicio para validar y registrar
        exito, mensaje = self.servicio.agregar_vehiculo(placa, marca, propietario)

        if exito:
            # Insertar nueva fila en la tabla
            self.tabla.insert("", "end", values=(
                placa.strip().upper(),
                marca.strip(),
                propietario.strip()
            ))

            # Actualizar etiqueta del total
            self.label_total.config(
                text=f"Total de vehiculos registrados: {self.servicio.total_vehiculos()}"
            )

            # Limpiar campos y mostrar confirmacion
            self._limpiar_campos()
            messagebox.showinfo("Exito", mensaje)

        else:
            messagebox.showerror("Error", mensaje)

    def _limpiar_campos(self):
        """
        Evento del boton Limpiar.
        Borra el contenido de todos los campos del formulario.
        """
        self.entry_placa.delete(0, tk.END)
        self.entry_marca.delete(0, tk.END)
        self.entry_propietario.delete(0, tk.END)
        self.entry_placa.focus()

    def iniciar(self):
        """Inicia el bucle principal de la ventana."""
        self.root.mainloop()