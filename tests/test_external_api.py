from src.external_api import convert_to_rub

import unittest
from unittest.mock import patch


class TestCurrencyConversion(unittest.TestCase):

    @patch('external_api.requests.get')
    def test_convert_to_rub_success(self, mock_get):
        # Настройка мока для успешного ответа от API
        mock_get.return_value.json.return_value = {'result': 1000.0}

        # Вызов функции с тестовыми данными
        result = convert_to_rub(100.0, 'USD')

        # Проверка, что результат соответствует ожидаемому значению
        self.assertEqual(result, 1000.0)

    @patch('external_api.requests.get')
    def test_convert_to_rub_failure(self, mock_get):
        # Настройка мока для неуспешного ответа от API
        mock_get.return_value.json.return_value = {}

        # Вызов функции с тестовыми данными
        result = convert_to_rub(100.0, 'USD')

        # Проверка, что результат равен None при ошибке
        self.assertIsNone(result)

    @patch('external_api.requests.get')
    def test_convert_to_rub_exception(self, mock_get):
        # Настройка мока для генерации исключения при запросе
        mock_get.side_effect = Exception("Network error")

        # Вызов функции с тестовыми данными
        result = convert_to_rub(100.0, 'USD')

        # Проверка, что результат равен None при возникновении исключения
        self.assertIsNone(result)
if __name__ == '__main__':
    unittest.main()
