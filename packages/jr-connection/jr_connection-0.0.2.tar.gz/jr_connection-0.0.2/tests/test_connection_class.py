import pytest
from unittest.mock import patch, MagicMock
from sqlalchemy.exc import SQLAlchemyError
from jr_connection.classes.connection_class import Connection

# from jr_connection.classes.dbconfig_class import DBConfig

import pytest
from unittest.mock import patch, MagicMock
from sqlalchemy.exc import SQLAlchemyError


# Mock credentials
mock_credentials = {
    "db_username": "user",
    "db_password": "pass",
    "db_host": "localhost",
    "db_name": "testdb",
    "db_driver": "ODBC Driver 17 for SQL Server",
}


@pytest.fixture
def mock_db_config():
    with patch(
        "jr_connection.classes.dbconfig_class.DBConfig.load_credentials",
        return_value=mock_credentials,
    ):
        yield


@pytest.fixture
def connection():
    with patch(
        "jr_connection.classes.connection_class.create_engine"
    ) as mock_create_engine:
        engine = mock_create_engine.return_value
        engine.begin.return_value.__enter__.return_value.execute.return_value.fetchone.return_value = (
            1,
        )
        conn = Connection()
        yield conn


def test_create_connection_string(mock_db_config):
    connection_string = Connection.create_connection_string(mock_credentials)
    assert (
        connection_string
        == f"mssql+pyodbc://{mock_credentials['db_username']}:{mock_credentials['db_password']}@{mock_credentials['db_host']}/{mock_credentials['db_name']}?driver={mock_credentials['db_driver']}&TrustServerCertificate=yes"
    )


def test_create_db_engine(connection):
    assert connection.engine is not None


def test_test_db_connection(connection):
    assert connection.test_db_connection() == True


def test_get_data(connection):
    with patch(
        "jr_connection.classes.connection_class.pd.read_sql_query"
    ) as mock_read_sql:
        mock_df = MagicMock()
        mock_read_sql.return_value = mock_df
        result_df = connection.get_data("test_table")
        assert result_df == mock_df
        mock_read_sql.assert_called_once()
