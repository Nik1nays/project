def get_mask_card_number(number_card: str) -> str:
    """Функция выводит маску карты"""
    if len(number_card) == 16:
        return f"{number_card[:4]} {number_card[4:6]}** **** {number_card[12:]}"
    return "Неверный ввод"


def get_mask_account(number_account: str) -> str:
    """Функция выводит последние 4 цифры номера счёта"""
    if len(number_account) == 20:
        return f"**{number_account[-4:]}"
    return "Неверный ввод данных"
