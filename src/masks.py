def get_mask_card_number(number_card: int) -> str:
    """Функция выводит маску карты"""
    number_card = str(number_card)
    if len(number_card) == 16:
        return f"{number_card[:4]} {number_card[4:6]}** **** {number_card[12:]}"
    return "Неверный ввод"


def get_mask_account(number_account: int) -> str:
    """Функция выводит последние 4 цифры номера счёта"""
    number_account = str(number_account)
    if len(number_account) == 20:
        return f"**{number_account[-4:]}"
    return "Неверный ввод данных"

