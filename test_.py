import pytest
from unittest.mock import MagicMock
from certificates_cmd import find_data


@pytest.fixture
def mock_google_sheets():
    """Фикстура для мока Google Sheets"""
    mock_client = MagicMock()
    mock_sheet = mock_client.open.return_value.sheet1
    mock_sheet.get_all_records.return_value = [
        {'name': 'Иванов Иван Иванович', 'certificate': '12345'},
        {'name': 'Мария Петрова', 'certificate': '67890'}
    ]
    return mock_client, mock_sheet


def test_find_data(mock_google_sheets):
    """Тестируем функцию поиска данных find_data"""
    _, mock_sheet = mock_google_sheets

    search_value = 'Иванов Иван Иванович'
    result = find_data(mock_sheet, search_value)
    assert result is not None

    assert result['name'] == search_value


def test_find_data_not_found(mock_google_sheets):
    """Тестируем отсутствие данных"""
    _, mock_sheet = mock_google_sheets

    search_value_not_found = 'Николай Николаев'
    result_not_found = find_data(mock_sheet, search_value_not_found)
    assert result_not_found is None
