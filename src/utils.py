import json
import os
from pathlib import Path

import data

def read_transactions_from_json(file_path):
    """
    Читает данные из JSON-файла.

    :param file_path: Путь к JSON-файлу.
    :return: Содержимое файла в виде словаря.
    :raises FileNotFoundError: Если файл не найден.
    :raises json.JSONDecodeError: Если файл содержит некорректный JSON.
    """
    file_path = os.path.abspath('data/operations.json')

    if not os.path.exists(file_path):
        print(f"Файл не найден: {file_path}")
        return []  # Возвращаем пустой список, если файл не найден

    with open(file_path, 'r', encoding='utf-8') as json_file:
        try:
            operations = json.load(json_file)
            if not isinstance(operations, list):
                return []  # Возвращаем пустой список, если содержимое не является списком
            return operations
        except json.JSONDecodeError:
            print("Ошибка декодирования JSON.")
            return []  # Возвращаем пустой список в случае ошибки декодирования JSON
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return []  # Возвращаем пустой список в случае других ошибок


# Пример использования функции
if __name__ == "__main__":
    # Путь к файлу с транзакциями

    file_path = os.path.join('operations.json')
    # Читаем транзакции из файла
    operations = read_transactions_from_json(file_path)

    # Выводим данные о транзакциях, если они есть
    if operations:
        for transaction in operations:
            print(transaction)
    else:
        print("Нет доступных транзакций.")