import os
import pandas as pd
from datetime import datetime
import json


class DataHandler:
    """
    Gestiona la recuperación y almacenamiento de datos desde la base de datos, asegurando que los datos están actualizados.

    Esta clase utiliza una instancia de conexión para recuperar datos de tablas especificadas y
    almacenar estos datos localmente en formato Parquet. Además, gestiona metadatos para asegurar
    que los datos no se actualizan innecesariamente.

    Atributos:
    ----------
    recipe_data_filename (str): Ruta del archivo donde se almacenan los datos de las recetas.
    metadata_filename (str): Ruta del archivo de metadatos que almacena la fecha de la última actualización.
    connection_instance (Connection): Instancia de la clase Connection para gestionar la conexión a la base de datos.
    tables (list): Lista de tablas para recuperar datos.
    update_frequency (str): Frecuencia de actualización de los datos ('daily' por defecto).

    Métodos:
    --------
    ensure_data_is_current(): Verifica y actualiza los datos si no están actualizados.
    check_data_exists(): Comprueba si existen datos almacenados localmente.
    check_update_needed(): Determina si es necesario actualizar los datos basado en la frecuencia y la última actualización.
    update_data_from_db(): Actualiza los datos desde la base de datos y los almacena localmente.
    write_metadata(): Escribe los metadatos actuales, incluyendo la fecha de última actualización.
    load_data(table_name): Carga datos desde un archivo local asegurando que están actualizados.
    """

    def __init__(
        self,
        connection_instance,
        tables,
        update_frequency="daily",
    ):
        """
        Inicializa el gestor de datos con una instancia de conexión, tablas específicas y la frecuencia de actualización.

        Parámetros:
        -----------
        connection_instance (Connection): La instancia de la clase Connection para realizar consultas a la base de datos.
        tables (list of str): Lista de nombres de las tablas de las cuales se recuperarán los datos.
        update_frequency (str): Frecuencia con la que se deben actualizar los datos ('daily' por defecto).

        Ejemplo:
        --------
        handler = DataHandler(connection, ['users', 'transactions'])
        """
        self.recipe_data_filename = "data/raw/JR_VW_MaestroRecetas.parquet"
        self.metadata_filename = "data/data_metadata.json"
        self.connection_instance = connection_instance
        self.tables = tables
        self.update_frequency = update_frequency

    def ensure_data_is_current(self):
        """
        Asegura que los datos almacenados son actuales verificando su existencia y necesidad de actualización.
        Si los datos no están actualizados, llama a update_data_from_db para actualizarlos.
        """
        if not self.check_data_exists() or self.check_update_needed():
            self.update_data_from_db()

    def check_data_exists(self):
        """
        Verifica si los datos ya están almacenados localmente.

        Retorna:
        --------
        bool
            True si el archivo de datos existe, False en caso contrario.
        """
        return os.path.exists(self.recipe_data_filename)

    def check_update_needed(self):
        """
        Comprueba si es necesario actualizar los datos basado en la última fecha de actualización almacenada y la frecuencia definida.

        Retorna:
        --------
        bool
            True si los datos necesitan ser actualizados, False en caso contrario.
        """
        if not os.path.exists(self.metadata_filename):
            return True

        with open(self.metadata_filename, "r") as file:
            metadata = json.load(file)
            last_update_str = metadata.get("last_updated", "1970-01-01")
            last_updated = datetime.strptime(last_update_str, "%Y-%m-%d").date()

        today = datetime.now().date()
        if self.update_frequency == "daily" and last_updated < today:
            return True
        return False

    def update_data_from_db(self):
        """
        Actualiza los datos desde la base de datos para todas las tablas especificadas y los almacena localmente.
        """
        if not self.connection_instance.is_connected:
            print("Database connection failed. Exiting...")
            return

        for table in self.tables:
            df = self.connection_instance.get_data(table)
            df.to_parquet(f"data/raw/{table}.parquet")

        self.write_metadata()

    def write_metadata(self):
        """
        Escribe los metadatos actualizados en el archivo de metadatos, incluyendo la fecha actual como fecha de última actualización.
        """
        today_str = datetime.now().strftime("%Y-%m-%d")
        with open(self.metadata_filename, "w") as file:
            json.dump({"last_updated": today_str}, file)

    def load_data(self, table_name):
        """
        Carga datos desde un archivo local, asegurando primero que los datos están actualizados.

        Parámetros:
        -----------
        table_name (str): Nombre del archivo de datos a cargar.

        Retorna:
        --------
        pandas.DataFrame
            DataFrame con los datos cargados.

        Ejemplo:
        --------
        df = handler.load_data('JR_VW_MaestroRecetas.parquet')
        """
        self.ensure_data_is_current()
        return pd.read_parquet(table_name)
