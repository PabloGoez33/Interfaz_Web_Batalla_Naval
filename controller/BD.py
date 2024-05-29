import psycopg2

from controller import SecretConfig

def GetCursor():
    """Crea la conexion a la base de datos y retorna un cursor para ejecutar instrucciones."""

    DATABASE = SecretConfig.PGDATABASE
    USER = SecretConfig.PGUSER
    PASSWORD = SecretConfig.PGPASSWORD
    HOST = SecretConfig.PGHOST
    PORT = SecretConfig.PGPORT

    connection = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)

    return connection.cursor()

class BD:
    """
    Clase que maneja la conexión y operaciones con la base de datos PostgreSQL.
    """

    def __init__(self):
        """
        Inicializa una conexión con la base de datos utilizando la cadena de conexión proporcionada.

        Args:
            connection_string (str): La cadena de conexión para conectarse a la base de datos.
        """
        try:
            self.cursor = GetCursor()
        except psycopg2.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
        

    def insert_victoria_jugador(self):
        """
        Inserta una nueva victoria del jugador en la base de datos.
        """
        self.cursor.execute("UPDATE estadisticas SET victorias_jugador = victorias_jugador + 1")
        self.cursor.connection.commit()

    def insert_derrota_jugador(self):
        """
        Inserta una nueva derrota del jugador en la base de datos.
        """
        self.cursor.execute("UPDATE estadisticas SET derrotas_jugador = derrotas_jugador + 1")
        self.cursor.connection.commit()

    def insert_victoria_ia(self):
        """
        Inserta una nueva victoria de la IA en la base de datos.
        """
        self.cursor.execute("UPDATE estadisticas SET victorias_ia = victorias_ia + 1")
        self.cursor.connection.commit()

    def insert_derrota_ia(self):
        """
        Inserta una nueva derrota de la IA en la base de datos.
        """
        self.cursor.execute("UPDATE estadisticas SET derrotas_ia = derrotas_ia + 1")
        self.cursor.connection.commit()

    def obtener_estadisticas(self):
        """
        Obtiene las estadísticas actuales de victorias y derrotas desde la base de datos.

        Returns:
            tuple: Una tupla que contiene el número de victorias del jugador, derrotas del jugador, victorias de la IA y derrotas de la IA.
        """
        self.cursor.execute("SELECT victorias_jugador, derrotas_jugador, victorias_ia, derrotas_ia FROM estadisticas")
        estadisticas = self.cursor.fetchone()
        return estadisticas

