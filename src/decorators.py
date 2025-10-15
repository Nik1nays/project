import time
from functools import wraps


def log(filename=None):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                start_func = time.time()
                result = func(*args, **kwargs)
                stop_func = time.time()
                log_massage = (f'Функция{func.__name__}\nВремя начала функции:{start_func}\n'
                               f'Время окончания:{stop_func}\nрезультат:{result}')
                if filename:
                    with open(filename, "a", encoding='utf-8') as log_file:
                        log_file.write(log_massage)
                else:
                    print(log_massage)
                return result
            except Exception as e:
                error_massage = (f'\nФункция {func.__name__}\n Тип ошибки:{e}\n'
                                 f'Входные параметры: {args}, {kwargs}')
                if filename:
                    with open(filename, 'a', encoding='utf-8') as log_file:
                        log_file.write(error_massage)
                else:
                    print(error_massage)
                raise
        return inner
    return wrapper


@log()
def my_function(x, y):
    return x + y

my_function(1, 2)