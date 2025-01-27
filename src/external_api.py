import os
import requests
from dotenv import load_dotenv
import utils

load_dotenv()  # Загружаем переменные окружения из .env

def convert_to_rub(amount, currency_code):
    """
    Конвертирует сумму из указанной валюты в рубли.

    :param amount: Сумма для конвертации.
    :param currency_code: Код валюты (например, 'USD', 'EUR').
    :return: Сумма в рублях или None в случае ошибки.
    """
    api_key = os.getenv('API_KEY')
    print(api_key)
    url = f'https://apilayer.com/exchangerates_data/convert?access_key={api_key}&from={currency_code}&to=RUB&amount={amount}'

    try:
        response = requests.get(url)
        data = response.json()
        print(data)
        if 'result' in data:
            return data['result']
        else:
            print("Ошибка при получении данных с API.")
            return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def convert_transaction_to_rub(transaction):
    """
    Конвертирует сумму транзакции в рубли.

    :param transaction: Словарь с данными о транзакции (должен содержать ключи 'amount' и 'currency').
    :return: Сумма транзакции в рублях (float).
    """
    amount = transaction['operationAmount']['amount']
    currency = transaction['operationAmount']['currency']['code']
    # Проверяем, что сумма и валюта указаны
    if amount is None or currency is None:
        print("Ошибка: сумма или валюта не указаны в транзакции.")
        return 0.0

    if currency == 'RUB':
        return float(amount)  # Если валюта уже в рублях, просто возвращаем сумму

    # Конвертация из USD или EUR в RUB
    if currency in ['USD', 'EUR']:
        converted_amount = convert_to_rub(float(amount), currency)
        return converted_amount if converted_amount is not None else 0.0

    # Если валюта не поддерживается, возвращаем 0.0
    print(f"Валюта {currency} не поддерживается.")
    return 0.0




if __name__ == "__main__":
    file_path = os.path.join('data', 'operations.json')

    transactions = utils.read_transactions_from_json(file_path)
    i=0
    print('data')
    for transaction in transactions:
        i+=1
        amount_in_rub = convert_transaction_to_rub(transaction)

        print(f"Сумма транзакции {i} в рублях: {amount_in_rub:.2f}")