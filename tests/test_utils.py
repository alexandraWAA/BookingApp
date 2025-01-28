# import os
#
# from src.decorators import log
#
#
# def test_read_transactions_from_json(tmp_path):
#     "Проверка: содержимое файла должно соответствовать ожидаемому"
#     file_name = "output.txt"
#     file_path = tmp_path / file_name
#
#     "Обновляем декоратор для использования временного пути"
#
#     @log(file_path)
#     def example_function():
#         return "Hello, World!"
#
#     "Вызов функции"
#     example_function()
#
#     "Проверка: файл должен существовать"
#     assert os.path.exists(file_path)