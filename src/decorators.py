import logging
import time

logging.basicConfig(level=logging.INFO)


def log(filename=None):
    def decorator(func):
        start_time = time.time()  # Запоминаем время начала выполнения

        def function(*args, **kwargs):
            if filename:
                with open(filename, "w") as file:
                    try:
                        "Объявление выполняемой функции"
                        result = func(*args, **kwargs)
                    except Exception as e:
                        "Если функция выдаст ошибку,то вывод функции ниже"
                        file.write(f"{func.__name__} error: {e} Inputs: {*args, {**kwargs}}")  # noqa: E501
                        return None
                    else:
                        file.write(f"{func.__name__} ok")
                        return result
            else:
                try:
                    "Объявление выполняемой функции"
                    result = func(*args, **kwargs)
                except Exception as e:
                    "Если функция выдаст ошибку,то вывод функции ниже"
                    print(f"{func.__name__} error: {e} Inputs: {*args, {**kwargs}}")  # noqa: E501
                    return None
                else:
                    print(f"{func.__name__} ok")
                    return result

        end_time = time.time()  # Запоминаем время окончания выполнения
        logging.info(f"Начало выполнения функции: {start_time}, Конец выполнения функции: {end_time}")  # noqa: E501
        return function

    return decorator


"""Проверка работы декоратора"""


@log()
def squares(x):
    return x * x


@log("file2.txt")
def sums(x):
    return x + x


if __name__ == "__main__":
    print(squares(3))
    print(sums(2))
