import os

import requests
from dotenv import load_dotenv
from utils import translations

load_dotenv()

API_KEY = os.getenv("API_KEY")


def operation_amount(translations: list[dict] | dict) -> float:
    """
    Функция возвращает сумму операции в рублях
    """
    for transaction in translations:
        if transaction != {}:
            currency = transaction.get('operationAmount').get('currency').get('code')
            amount_cur = float(transaction.get('operationAmount').get('amount'))
            if currency == 'RUB':
                amount = amount_cur
                print(amount)
            else:
                payload = {}
                headers = {
                    "apikey": API_KEY
                }
                response = requests.request("GET", f"https://api.apilayer.com/exchangerates_data/convert?to={'RUB'}&from={currency}&amount={amount_cur}", headers=headers, data=payload)

                status_code = response.status_code
                print(status_code)
                if status_code == 200:
                    result = response.json()
                    print(result)
                    amount = round(float(result.get('result')), 2)
                    print(amount)
        else:
            pass


operation_amount(translations)
