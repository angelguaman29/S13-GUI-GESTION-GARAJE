# ontiene la logica del sistema. Gestiona la lista de vehiculos registrados en el garaje.

from modelos.vehiculo import Vehiculo


class GarajeServicio:
    """
    Clase que gestiona los vehiculos del garaje.

    Colecciones utilizadas:
        __vehiculos (list) : Lista de objetos Vehiculo registrados.
        __placas    (set)  : Conjunto de placas para evitar duplicados.
    """

    def __init__(self):
        """Constructor: inicializa la lista y el conjunto vacios."""
        # LISTA: almacena los vehiculos en orden de registro
        self.__vehiculos = []

        # CONJUNTO: placas registradas para detectar duplicados en O(1)
        self.__placas = set()

    def agregar_vehiculo(self, placa, marca, propietario):
        """
        Crea y registra un nuevo vehiculo en el garaje.

        Parametros:
            placa       (str) : Placa del vehiculo.
            marca       (str) : Marca del vehiculo.
            propietario (str) : Nombre del propietario.

        Retorna:
            tuple: (bool, str) exito y mensaje para mostrar en la UI.
        """
        # Validar que los campos no esten vacios
        if not placa.strip() or not marca.strip() or not propietario.strip():
            return False, "Todos los campos son obligatorios."

        # Verificar placa duplicada usando el conjunto
        if placa.strip().upper() in self.__placas:
            return False, f"Ya existe un vehiculo con la placa '{placa.upper()}'."

        # Crear el objeto Vehiculo y agregarlo a la lista
        vehiculo = Vehiculo(placa, marca, propietario)
        self.__vehiculos.append(vehiculo)
        self.__placas.add(vehiculo.get_placa())

        return True, f"Vehiculo '{placa.upper()}' registrado correctamente."

    def obtener_vehiculos(self):
        """
        Retorna la lista completa de vehiculos registrados.

        Retorna:
            list: Lista de objetos Vehiculo.
        """
        return self.__vehiculos

    def total_vehiculos(self):
        """
        Retorna el numero total de vehiculos en el garaje.

        Retorna:
            int: Cantidad de vehiculos registrados.
        """
        return len(self.__vehiculos)