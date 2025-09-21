from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_input: str) -> str:
    """Функция определяет тип и делает маскировку"""
    if "счет" in user_input.lower():
        return f"Счет {get_mask_account(user_input[-20:])}"
    elif user_input[-16:].isdigit():
        return f"{user_input[:-16]}{get_mask_card_number(user_input[-16:])}"
    return "Неверно введены данные"


def get_date(date_str: str) -> str:
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")




