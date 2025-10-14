import time
from functools import wraps


def log(filename):
    def wrapper(funk):
        @wraps
        def inner(*args, **kwargs):
            try:
                start_funk = time.time()
                result = funk(*args, **kwargs)
                end_funk = time.time()
                log_message = f"Функция: {funk.__name__}\n Время начала выполнения функции: {start_funk}\n Время окончания выполнения функции: {end_funk}\n Результат: {result}\n"
                if filename:
                    with open(filename, "a") as log_file:
                        log_file.write(log_message)
                else:
                    print(log_message)
                return result

            except Exception as e:
                error_message = f"Функция: {funk.__name__}\n Тип ошибки: {e} \n Входные параметры: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a") as log_file:
                        log_file.write(error_message)
                else:
                    print(error_message)
                raise

        return inner

    return wrapper

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)