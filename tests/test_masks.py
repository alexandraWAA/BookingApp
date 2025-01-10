import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "number, expected",
    [
        ("Счет 1596837868705199908", "**9908"),
        ("Счет 64686473678894779589", "**9589"),
        ("Счет 6468647367889477", "**9477"),
        ("Счет 64686367889477", "**9477"),
    ],
)
def test_get_mask_account(number, expected):
    assert get_mask_account(number) == expected


@pytest.mark.parametrize(
    "number, expected",
    [
        ("1596 886 00", "Введите корректный номер карты"),
        ("159688463636987840", "1596 8846** **** 7840"),
        ("", "Введите корректный номер карты"),
    ],
)
def test_mask_card_number(number, expected):

    assert get_mask_card_number(number) == expected
