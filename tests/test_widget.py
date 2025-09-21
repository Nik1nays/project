import pytest

from src.widget import mask_account_card, get_date


def test_mask_account_card():
    assert mask_account_card("Maestro 1596837868705199") == 'Maestro 1596 83** **** 5199'
    assert mask_account_card("Счет 64686473678894779589") == "Счет **9589"
    assert mask_account_card("") == "Неверно введены данные"



@pytest.mark.parametrize('value, expected', [
    ('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
    ('Счет 73654108430135874305', 'Счет **4305')
    ])
def test2_mask_account_card(value, expected):
    assert mask_account_card(value) == expected

def test_get_date():
    assert get_date('2024-03-11T02:26:18.671407') == '11.03.2024'


with pytest.raises(ValueError) as exc_info:
    get_date('2024.03.11T02:26:18.671407')

    assert str(exc_info.value) == 'Неверный формат даты'