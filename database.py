import json
import os

products = []
sales = []

def save_data():
    with open("products.json", "w", encoding="utf-8") as f:
        json.dump(products, f, indent=4)
    with open("sales.json", "w", encoding="utf-8") as f:
        json.dump(sales, f, indent=4)

def load_data():
    global products, sales
    
    if os.path.exists("products.json"):
        try:
            with open("products.json", "r", encoding="utf-8") as f:
                loaded = json.load(f)
                products.clear()
                products.extend(loaded)
        except json.JSONDecodeError:
            pass

    if os.path.exists("sales.json"):
        try:
            with open("sales.json", "r", encoding="utf-8") as f:
                loaded = json.load(f)
                sales.clear()
                sales.extend(loaded)
        except json.JSONDecodeError:
            pass