import json


def read_json(path: str) -> list[dict] | dict:
    """Чтение json файла"""
    try:
        with open(path, encoding='utf-8') as json_file:
            json_dict = json.load(json_file)
            return json_dict
    except FileNotFoundError:
        return []

translations = read_json('../data/operations.json')
