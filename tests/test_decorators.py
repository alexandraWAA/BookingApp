import os

from src.decorators import log


@log()
def squares(x):
    return x * x


@log("file.txt")
def sums(x):
    return x + x


def test_log():
    "Тест успешного выполнения функции"

    assert sums(2) == 4


def test_save_to_file_by_log(tmp_path):
    "Проверка: содержимое файла должно соответствовать ожидаемому"
    file_name = "output.txt"
    file_path = tmp_path / file_name

    "Обновляем декоратор для использования временного пути"

    @log(file_path)
    def example_function():
        return "Hello, World!"

    "Вызов функции"
    example_function()

    "Проверка: файл должен существовать"
    assert os.path.exists(file_path)

    "Проверка: содержимое файла должно соответствовать ожидаемому"
    with open(file_path, "r") as f:
        content = f.read()
        assert content == "example_function ok"


def test_log_with_error(tmp_path):
    "Проверка выбрасывания ошибки и записи ее в файл"
    file_name = "output.txt"
    file_path = tmp_path / file_name

    @log(file_path)
    def squares(x):
        return x * x

    squares("3")

    with open(file_path, "r") as f:
        content = f.read()
        assert content == ("squares error: can't multiply sequence by non-int of type 'str'" " Inputs: ('3', {})")  # noqa: E501


def test_console_output(capsys):
    "Проверка вывода результата в консоль"
    squares(3)
    captured = capsys.readouterr()
    assert "squares ok\n" in captured.out
