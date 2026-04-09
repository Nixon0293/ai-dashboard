import requests
import json

RETAIL_URL = "https://nixon0293.retailcrm.ru"
API_KEY = "dckOcQjessIfeRLaXGCosdcMlxSyIyii"

SUPABASE_URL = "https://ibvlgosbjpntuorpwyiy.supabase.co"
SUPABASE_KEY = "sb_publishable_9Y0g__k5__PGW23QrLRbYg_OyGlxuba"

def get_orders():
    url = f"{RETAIL_URL}/api/v5/orders"
    params = {"apiKey": API_KEY, "limit": 100}
    response = requests.get(url, params=params)
    return response.json().get("orders", [])

def save_to_supabase(orders):
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json"
    }
    
    for order in orders:
        total = 0
        for item in order.get("items", []):
            total += item.get("initialPrice", 0) * item.get("quantity", 1)
        
        data = {
            "external_id": order.get("externalId"),
            "customer_name": f"{order.get('firstName', '')} {order.get('lastName', '')}".strip(),
            "phone": order.get("phone", ""),
            "email": order.get("email", ""),
            "total_sum": total,
            "created_at": order.get("createdAt")
        }
        
        if not data["external_id"]:
            continue
        
        # Проверяем, есть ли уже такой заказ
        check = requests.get(
            f"{SUPABASE_URL}/rest/v1/orders?external_id=eq.{data['external_id']}",
            headers=headers
        )
        
        if check.status_code == 200 and len(check.json()) > 0:
            print(f"⏩ Заказ {data['external_id']} уже существует")
            continue
        
        # Добавляем новый заказ
        response = requests.post(
            f"{SUPABASE_URL}/rest/v1/orders",
            headers=headers,
            json=data
        )
        
        if response.status_code == 201:
            print(f"✅ Сохранён заказ {data['external_id']}")
        else:
            print(f"❌ Ошибка {data['external_id']}: {response.text}")

if __name__ == "__main__":
    orders = get_orders()
    print(f"📦 Найдено заказов в RetailCRM: {len(orders)}")
    save_to_supabase(orders)
    print("🎉 Готово!")
