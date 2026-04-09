import requests
import json

RETAIL_URL = "https://nixon0293.retailcrm.ru"
API_KEY = "dckOcQjessIfeRLaXGCosdcMlxSyIyii"

# Загружаем заказы из файла
with open("mock_orders.json", "r", encoding="utf-8") as file:
    orders = json.load(file)

for i, order_data in enumerate(orders):
    # Формируем заказ в нужном формате
    new_order = {
        "externalId": str(i + 1),
        "firstName": order_data.get("firstName", ""),
        "lastName": order_data.get("lastName", ""),
        "phone": order_data.get("phone", ""),
        "email": order_data.get("email", ""),
        "orderMethod": "shopping-cart",
        "status": "new",
        "createdAt": "2025-04-09 12:00:00",
        "items": [
            {
                "productName": item.get("productName", "Товар"),
                "quantity": item.get("quantity", 1),
                "initialPrice": item.get("initialPrice", 1000),
                "price": item.get("initialPrice", 1000)
            }
            for item in order_data.get("items", [])
        ],
        "delivery": {
            "code": "self"
        }
    }
    
    payload = {"order": json.dumps(new_order)}
    url = f"{RETAIL_URL}/api/v5/orders/create"
    params = {"apiKey": API_KEY}
    
    response = requests.post(url, params=params, data=payload)
    
    if response.status_code == 200:
        print(f"✅ Заказ {i+1} загружен")
    else:
        print(f"❌ Заказ {i+1}: {response.text}")

print("Готово!")
