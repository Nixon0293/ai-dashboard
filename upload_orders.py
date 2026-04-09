import requests
import json

RETAIL_URL = "https://nixon0293.retailcrm.ru"
API_KEY = "dckOcQjessIfeRLaXGCosdcMlxSyIyii"

# Минимально правильный заказ для RetailCRM
test_order = {
    "externalId": "test_001",
    "firstName": "Тест",
    "lastName": "Тестов",
    "phone": "+79991234567",
    "email": "test@example.com",
    "orderType": "fiz",
    "orderMethod": "phone",
    "status": "new",
    "createdAt": "2025-04-09 12:00:00",
    "items": [
        {
            "productName": "Тестовый товар",
            "quantity": 1,
            "initialPrice": 1000,
            "price": 1000
        }
    ],
    "delivery": {
        "code": "self"
    }
}

payload = {"order": test_order}
url = f"{RETAIL_URL}/api/v5/orders/create"
params = {"apiKey": API_KEY}

response = requests.post(url, params=params, json=payload)

print(f"Статус: {response.status_code}")
print(f"Ответ: {response.text}")
