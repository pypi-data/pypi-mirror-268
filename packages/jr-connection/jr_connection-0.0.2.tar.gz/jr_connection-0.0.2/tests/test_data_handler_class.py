import pytest
from unittest.mock import patch, MagicMock, mock_open
from jr_connection.classes.data_handler_class import DataHandler
from jr_connection.classes.connection_class import Connection
import pandas as pd
from datetime import date


@pytest.fixture
def mock_connection():
    with patch("jr_connection.classes.connection_class.Connection") as MockConnection:
        conn_instance = MockConnection()
        conn_instance.is_connected = True
        conn_instance.get_data = MagicMock(
            return_value=pd.DataFrame({"data": [1, 2, 3]})
        )
        yield conn_instance


def test_check_data_exists(data_handler):
    with patch(
        "jr_connection.classes.data_handler_class.os.path.exists", return_value=True
    ):
        assert data_handler.check_data_exists() == True


def test_check_update_needed_no_metadata(data_handler):
    with patch(
        "jr_connection.classes.data_handler_class.os.path.exists", return_value=False
    ):
        assert data_handler.check_update_needed() == True


@pytest.fixture
def data_handler(mock_connection):
    return DataHandler(connection_instance=mock_connection, tables=["test_table"])


@patch("datetime.date")
def test_check_update_needed_with_metadata(mock_date_class, data_handler):
    mock_date_class.today.return_value = date(2023, 4, 15)
    with patch(
        "jr_connection.classes.data_handler_class.os.path.exists", return_value=True
    ), patch(
        "builtins.open", mock_open(read_data='{"last_updated": "2023-04-14"}')
    ), patch(
        "jr_connection.classes.data_handler_class.json.load",
        return_value={"last_updated": "2023-04-14"},
    ):
        assert data_handler.check_update_needed() == True


def test_update_data_from_db(data_handler, mock_connection):
    with patch(
        "jr_connection.classes.connection_class.pd.DataFrame.to_parquet"
    ) as mock_to_parquet, patch("builtins.open", mock_open()):
        data_handler.update_data_from_db()
        assert mock_connection.get_data.called
        assert mock_to_parquet.called


def test_load_data(data_handler):
    with patch(
        "jr_connection.classes.data_handler_class.DataHandler.ensure_data_is_current"
    ) as mock_ensure, patch(
        "jr_connection.classes.data_handler_class.pd.read_parquet",
        return_value=pd.DataFrame({"data": [1, 2, 3]}),
    ):
        df = data_handler.load_data("test_table.parquet")
        assert df.equals(pd.DataFrame({"data": [1, 2, 3]}))
        assert mock_ensure.called
