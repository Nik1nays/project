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


if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ],
            state="CANCELED",
        )
    )


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


if __name__ == "__main__":
    print(
        sort_by_date(
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ]
        )
    )
