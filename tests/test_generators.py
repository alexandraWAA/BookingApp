from src.generators import (
    get_card_number_generator,
    get_filter_by_currency,
    get_transaction_descriptions,
)

transactions = [
    {
        "operationAmount": {"currency": {"code": "USD"}},
        "description": "Перевод организации a",
    },
    {
        "operationAmount": {"currency": {"code": "EUR"}},
        "description": "Перевод организации б",
    },
    {
        "operationAmount": {"currency": {"code": "USD"}},
        "description": "Перевод организации с",
    },
    {
        "operationAmount": {"currency": {"code": "RUB"}},
        "description": "Перевод организации д",
    },
]


def test_get_filter_by_currency(usd_transactions):

    assert next(get_filter_by_currency(transactions, "USD")) == usd_transactions


def test_get_transaction_descriptions(first_transaction_descriptions):
    assert next(get_transaction_descriptions(transactions)) == first_transaction_descriptions


def test_get_card_number_generator():
    assert next(get_card_number_generator(111111111, 111111119)) == "0000 0001 1111 1111"