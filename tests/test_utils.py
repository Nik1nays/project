from src.utils import read_json


def test_read_json:
    result = read_json("..//data/fake_file")
    assert result == []