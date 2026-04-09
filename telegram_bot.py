import requests
import time

RETAIL_URL = "https://nixon0293.retailcrm.ru"
API_KEY = "dckOcQjessIfeRLaXGCosdcMlxSyIyii"
BOT_TOKEN = "8303834127:AAEDkDu6SXMBndJ1HwGcZ9-vidb5oN-nCLU"
CHAT_ID = "855917320"

def check_orders():
    url = f"{RETAIL_URL}/api/v5/orders"
    params = {"apiKey": API_KEY, "limit": 20}
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        print(f"Ошибка API: {response.status_code}")
        return
        
    orders = response.json().get("orders", [])
    print(f"Найдено заказов: {len(orders)}")
    
    for order in orders:
        total = sum(item.get("initialPrice", 0) * item.get("quantity", 1) 
                   for item in order.get("items", []))
        if total > 1:  # порог 1 — для теста
            msg = f"🔥 Новый заказ >1₸! Заказ №{order.get('externalId')} на сумму {total}₸"
            url_send = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            requests.post(url_send, json={"chat_id": CHAT_ID, "text": msg})
            print(f"Отправлено: {msg}")

if __name__ == "__main__":
    print("Бот запущен. Проверка каждую минуту...")
    while True:
        check_orders()
        time.sleep(60)
