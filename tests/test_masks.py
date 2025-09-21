from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("700079228960636125235") == "Неверный ввод"
    assert get_mask_card_number("7000792289235") == "Неверный ввод"
    assert get_mask_card_number("") == "Неверный ввод"

def test_get_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("7365410843074305") == "Неверный ввод данных"
    assert get_mask_account("7365410843013567567874305") == "Неверный ввод данных"
    assert get_mask_account("") == "Неверный ввод данных"

