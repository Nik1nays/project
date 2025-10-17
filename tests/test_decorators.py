import pytest

from src.decorators import my_function, log


# функция для теста
def divide_num(a, b):
    return a / b


@log()
def test_my_function(capsys):
    result = my_function(1, 2)
    captured = capsys.readouterr()
    assert result == 3
    assert "my_function ok" in captured.out


@log()
def test_err_function():
    with pytest.raises(ZeroDivisionError):
        divide_num(1, 0)
