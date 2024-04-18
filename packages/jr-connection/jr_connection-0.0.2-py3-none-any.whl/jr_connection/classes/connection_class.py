# connection_class.py

# Related Third Library Imports
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# Local Application/Library Specific Imports
from .dbconfig_class import DBConfig

class Connection:
    """
    Gestiona la conexión a la base de datos y las operaciones de recuperación de datos.

    Esta clase se encarga de establecer la conexión con la base de datos usando las credenciales
    cargadas y proporciona métodos para obtener datos de la base de datos y almacenarlos localmente.

    Atributos:
    ----------
    credentials (dict): Credenciales cargadas para la conexión a la base de datos.
    connection_string (str): Cadena de conexión a la base de datos construida a partir de las credenciales.
    engine (sqlalchemy.engine.base.Engine): Motor de base de datos para ejecutar consultas.
    is_connected (bool): Estado de la conexión, True si la conexión fue exitosa.

    Métodos:
    --------
    create_connection_string(credentials): Construye una cadena de conexión usando las credenciales proporcionadas.
    create_db_engine(): Crea y retorna un motor de base de datos.
    test_db_connection(): Verifica y retorna el estado de la conexión a la base de datos.
    get_data(table_name): Recupera datos de una tabla especificada y los almacena como archivos Parquet.
    """
     
    def __init__(self):
        """
        Inicializa la conexión a la base de datos cargando las credenciales, construyendo la cadena
        de conexión, creando el motor de base de datos y verificando la conexión.
        """
        self.credentials = DBConfig.load_credentials()
        self.connection_string = self.create_connection_string(self.credentials)
        self.engine = self.create_db_engine()
        self.is_connected = self.test_db_connection()

    @staticmethod
    def create_connection_string(credentials):
        """
        Construye una cadena de conexión a la base de datos a partir de las credenciales proporcionadas.

        Parámetros:
        -----------
        credentials (dict): Diccionario con las credenciales de la base de datos.

        Retorna:
        --------
        str
            La cadena de conexión formateada.

        Ejemplo:
        --------
        credentials = {'db_username': 'user', 'db_password': 'pass', 'db_host': 'localhost', 'db_name': 'mydb', 'db_driver': 'ODBC Driver 17 for SQL Server'}
        connection_string = Connection.create_connection_string(credentials)
        """
        return f"mssql+pyodbc://{credentials['db_username']}:{credentials['db_password']}@{credentials['db_host']}/{credentials['db_name']}?driver={credentials['db_driver']}&TrustServerCertificate=yes"

    def create_db_engine(self):
        """
        Intenta crear y retorna un motor de base de datos utilizando la cadena de conexión.

        Retorna:
        --------
        sqlalchemy.engine.base.Engine or None
            Motor de base de datos si la creación es exitosa, None si ocurre un error.

        Ejemplo:
        --------
        engine = self.create_db_engine()
        """
        try:
            engine = create_engine(self.connection_string)
            return engine
        except SQLAlchemyError as e:
            print(f"Error! : {e}")
            return None

    def test_db_connection(self):
        """
        Verifica la conexión a la base de datos intentando ejecutar una consulta simple.

        Retorna:
        --------
        bool
            True si la conexión es exitosa, False si falla.

        Ejemplo:
        --------
        is_connected = self.test_db_connection()
        """
        try:
            with self.engine.begin() as conn:
                result = conn.execute(text("SELECT 1"))
                result.fetchone()
                self.is_connected = True
                return self.is_connected
        except Exception as e:
            self.is_connected = False
            return self.is_connected


    def get_data(self, table_name):
        """
        Recupera datos de la tabla especificada y los almacena localmente en formato Parquet.

        Parámetros:
        -----------
        table_name (str): Nombre de la tabla de la cual se recuperarán los datos.

        Retorna:
        --------
        pandas.DataFrame
            DataFrame de pandas que contiene los datos recuperados.

        Ejemplo:
        --------
        df = self.get_data('tabla')
        """
        with self.engine.begin() as conn:
            query = text(f"""
                    SELECT *
                    FROM {table_name}
                    """
                )
            df = pd.read_sql_query(query, conn)
            df.to_parquet(f"./data/raw/{f"{table_name}.parquet"}")
        return df


