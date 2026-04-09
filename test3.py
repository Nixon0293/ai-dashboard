import requests
import json

RETAIL_URL = "https://nixon0293.retailcrm.ru"
API_KEY = "dckOcQjessIfeRLaXGCosdcMlxSyIyii"

test_order = {
    "externalId": "test_004",
    "firstName": "Иван",
    "lastName": "Тестов",
    "phone": "+79991234567",
    "email": "test4@example.com",
    "orderMethod": "phone",
    "status": "new",
    "createdAt": "2025-04-09 12:00:00",
    "items": [
        {
            "productName": "Товар",
            "quantity": 1,
            "initialPrice": 1000,
            "price": 1000
        }
    ],
    "delivery": {
        "code": "self"
    }
}

payload = {"order": json.dumps(test_order)}
url = f"{RETAIL_URL}/api/v5/orders/create"
params = {"apiKey": API_KEY}

response = requests.post(url, params=params, data=payload)

print(f"Статус: {response.status_code}")
print(f"Ответ: {response.text}")

