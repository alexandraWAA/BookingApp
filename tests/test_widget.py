import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "number, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 6468647367", "Введите корректный номер счета"),
        ("Счет ", "Введите корректный номер счета"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет avfs", "Введите корректный номер счета"),
    ],
)
def test_mask_account_card(number, expected):
    assert mask_account_card(number) == expected


@pytest.mark.parametrize(
    "day, expected",
    [("", "Введите корректные данные"), ("2024-03-11T02:26:18.671407", "11.03.2024")],
)
def test_get_data(day, expected):
    assert get_date(day) == expected
