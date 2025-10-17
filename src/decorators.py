import time
from functools import wraps


def log(filename=None):
    """
    Декоратор, который автоматически логирует начало и конец функции
    """
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                start_func = time.time()
                result = func(*args, **kwargs)
                stop_func = time.time()
                log_massage = (
                    f"{func.__name__} ok"
                )
                print(f'Функция выполнялась: {stop_func - start_func}\n'
                      f'Результат: {result}')
                if filename:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(log_massage)
                else:
                    print(log_massage)
                return result
            except Exception as e:
                error_massage = (
                    f"{func.__name__}\n error:{e}\n"
                    f"Inputs: {args}, {kwargs}"
                )
                if filename:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(error_massage)
                else:
                    print(error_massage)
                raise

        return inner

    return wrapper


@log(filename="../mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)
