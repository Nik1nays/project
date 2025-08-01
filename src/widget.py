from masks import get_mask_account
from masks import get_mask_card_number

def mask_account_card(user_input: str) -> str:
    """Функция определяет тип и делает маскировку"""
    if "счет" in user_input.lower():
        number_account = int(user_input[-20:])
        return f"Счет {str(get_mask_account(number_account))}"
    elif user_input[-16:].isdigit():
        return f"{user_input[:-16]}{get_mask_card_number(int(user_input[-16:]))}"
    return "Неверно введены данные"


if __name__ == '__main__':
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("MasterCard 7158300734726758"))
    print(mask_account_card("Счет 35383033474447895560"))
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(mask_account_card("Счет 73654108430135874305"))


def get_date(user_date: str) -> str:
    return f"{user_date[8:10]}.{user_date[5:7]}.{user_date[:4]}"

if __name__ == '__main__':
    print(get_date("2024-03-11T02:26:18.671407"))