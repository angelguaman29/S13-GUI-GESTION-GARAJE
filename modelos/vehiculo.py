# Define la clase Vehiculo con sus atributos privados y metodos getter/setter.



class Vehiculo:
    """
    Clase que representa un vehiculo registrado en el garaje.

    Atributos privados:
        __placa       (str) : Placa unica del vehiculo.
        __marca       (str) : Marca del vehiculo (ej: Toyota).
        __propietario (str) : Nombre del propietario.
    """

    def __init__(self, placa, marca, propietario):
        """
        Constructor de la clase Vehiculo.

        Parametros:
            placa       (str) : Placa del vehiculo.
            marca       (str) : Marca del vehiculo.
            propietario (str) : Nombre del propietario.
        """
        # Atributos privados (encapsulamiento)
        self.__placa       = placa.strip().upper()
        self.__marca       = marca.strip()
        self.__propietario = propietario.strip()

    # --------------------------------------------------------
    # GETTERS: permiten leer los atributos privados
    # --------------------------------------------------------

    def get_placa(self):
        """Retorna la placa del vehiculo."""
        return self.__placa

    def get_marca(self):
        """Retorna la marca del vehiculo."""
        return self.__marca

    def get_propietario(self):
        """Retorna el nombre del propietario."""
        return self.__propietario

    # --------------------------------------------------------
    # SETTERS: permiten modificar atributos con validacion
    # --------------------------------------------------------

    def set_placa(self, placa):
        """Establece una nueva placa. Valida que no este vacia."""
        if placa.strip() == "":
            print("Error: la placa no puede estar vacia.")
        else:
            self.__placa = placa.strip().upper()

    def set_marca(self, marca):
        """Establece una nueva marca. Valida que no este vacia."""
        if marca.strip() == "":
            print("Error: la marca no puede estar vacia.")
        else:
            self.__marca = marca.strip()

    def set_propietario(self, propietario):
        """Establece un nuevo propietario. Valida que no este vacio."""
        if propietario.strip() == "":
            print("Error: el propietario no puede estar vacio.")
        else:
            self.__propietario = propietario.strip()

    # --------------------------------------------------------
    # REPRESENTACION EN TEXTO
    # --------------------------------------------------------

    def __str__(self):
        """Devuelve una representacion legible del vehiculo."""
        return (
            f"Placa: {self.__placa:<10} | "
            f"Marca: {self.__marca:<15} | "
            f"Propietario: {self.__propietario}"
        )