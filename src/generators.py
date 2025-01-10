def get_filter_by_currency(transactions, bill="RUB"):
    """Функция выдачи транзакции заданной валюты"""
    return (el for el in transactions if el["operationAmount"]["currency"]["code"] == bill)


def get_transaction_descriptions(transactions):
    """Функция выдачи описания каждой транзакции"""
    for transaction in transactions:
        yield transaction["description"]


def get_card_number_generator(el_start: int, el_stop: int):
    """Функция генератора номера банковской карты"""
    nums = list(str(x).zfill(16) for x in range(el_start, (el_stop + 1)))
    num = 0
    while True:
        yield nums[num][:4] + " " + nums[num][4:8] + " " + nums[num][8:12] + " " + nums[num][12:]
        num += 1


if __name__ == "__main__":
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

    filtered_result = get_filter_by_currency(transactions, "USD")
    "Вывод {'operationAmount': {'currency': {'code': 'USD'}}, 'description': 'Перевод организации a'}"
    print(next(filtered_result))
    "Вывод {'operationAmount': {'currency': {'code': 'USD'}}, 'description': 'Перевод организации с'}"
    print(next(filtered_result))

    descriptions = get_transaction_descriptions(transactions)
    "Вывод: Перевод организации a, Перевод организации б"
    for num in range(2):
        print(next(descriptions))

    numbers = get_card_number_generator(111111111, 111111119)
    "Вывод: 0000 0001 1111 1111, 0000 0001 1111 1112, 0000 0001 1111 1113"
    for num in range(3):
        print(next(numbers))
