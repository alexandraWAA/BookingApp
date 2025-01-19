import logging
import time

logging.basicConfig(level=logging.INFO)

"""Объявление декоратора логирования функции"""

def log(filename=None):
    def decorator(func):
        """Регистрация начала работы функции"""
        start_time = time.time()  # Запоминаем время начала выполнения
        def function(*args, **kwargs):
            """Блок проверки наличия файла для записи результата функции"""
            if filename:
                """Открываем документ для записи файла"""
                with open(filename, "w") as file:
                    try:
                        """Объявление выполняемой функции с аргументами"""
                        result = func(*args, **kwargs)
                    except Exception as e:
                        """Если функция выдаст любую ошибку,то в файл будет записан следующий вывод, содержащий наименование ошибки и передаваемые параметры"""  # noqa: E501
                        file.write(f"{func.__name__} error: {e} Inputs: {*args, {**kwargs}}")  # noqa: E501
                        return None
                    else:
                        """Если функция не выдаст ошибку,то в файл будет записано название функции и ее статус"""  # noqa: E501

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
        """Регистрация конца работы функции"""
        end_time = time.time()  # Запоминаем время окончания выполнения
        """Запись времени и выдача этой информации"""
        logging.info(f"Начало выполнения функции: {start_time}, Конец выполнения функции: {end_time}")  # noqa: E501
        return function

    return decorator



"""Объявление двух функций"""

@log()
def squares(x):
    return x * x


@log("file2.txt")
def sums(x):
    return x + x

"""Проверка работы декоратора"""
if __name__ == "__main__":
    print(squares(3))
    print(sums(2))
