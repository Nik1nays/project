from datetime import datetime


def filter_by_state(info_user: list, state="EXECUTED") -> list:
    """ "Функция сортирует по указанному значению 'state'"""
    user_executed = []
    for meaning in info_user:
        if meaning["state"] == state:
            user_executed.append(meaning)
        else:
            continue
    return user_executed


def sort_by_date(list_user: list, reverse=True) -> list:
    """Функция сортирует список по дате, по умолчанию в обратном порядке"""
    if reverse == True:
        return sorted(
            list_user,
            key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"),
            reverse=True,
        )
    else:
        return sorted(
            list_user,
            key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"),
        )
