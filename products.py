import database
from database import products

def add_products():
    print("\n--- ADD PRODUCTS ---")

    while True:
        name = input("What is the name of the product? ").strip()
        if name == "":
            print("Invalid input. Name cannot be empty.")
            continue
        if name.isdigit():
            print("Invalid input. Name cannot be a number.")
            continue
        break

    while True:
        category = input("What is the category of the product? ").strip()
        if category == "":
            print("Invalid input. Category cannot be empty.")
            continue
        if category.isdigit():
            print("Invalid input. Category cannot be a number.")
            continue
        break

    while True:
        try:
            price = float(input("What is the price of the product? "))
            if price <= 0:
                print("Invalid input. Price must be a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the price.")

    while True:
        try:
            quantity = int(input("How many are you getting? "))
            if quantity <= 0:
                print("Invalid input. Quantity must be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid whole number for the quantity.")

    new_id = len(products) + 1

    product = {
        "generated_product_id": new_id,
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity
    }
    products.append(product)
    database.save_data()
    print(f"Product added successfully with ID: {new_id}!")

def view_products():
    print("\n--- VIEW PRODUCTS ---")
    if len(products) == 0:
        print("No products found")
    else:
        print("Your product available:")
        for p in products:
            print(p)

def update_products():
    print("\n--- UPDATED PRODUCTS ---")
    try:
        user_id = int(input("What is the generated_product_id? "))
    except ValueError:
        print("Invalid input. ID must be a number.")
        return
        
    for p in products:
        if user_id == p["generated_product_id"]:
            p["name"] = input(f"New name [{p['name']}]: ") or p['name']
            p["category"] = input(f"New category [{p['category']}]: ") or p['category']
            try:
                new_price = input(f"New price [{p['price']}]: ")
                if new_price: p["price"] = float(new_price)
                new_qty = input(f"New quantity [{p['quantity']}]: ")
                if new_qty: p["quantity"] = int(new_qty)
            except ValueError:
                print("Invalid number format.")
                return
            database.save_data()
            print("Product updated successfully")
            break
    else:
        print("Product not found")

def delete_products():
    print("\n--- DELETED PRODUCTS ---")
    try:
        user_id = int(input("What is the generated_product_id? "))
    except ValueError:
        print("Invalid input. ID must be a number.")
        return
        
    for p in products:
        if user_id == p["generated_product_id"]:
            products.remove(p)
            
            for index, prod in enumerate(products, start=1):
                prod["generated_product_id"] = index
                
            database.save_data()
            print("Product deleted and IDs re-indexed successfully!")
            break
    else:
        print("Product not found")

def check_stock_availability():
    print("\n--- CHECK STOCK AVAILABILITY ---")
    try:
        user_id = int(input("What is the generated_product_id? "))
        demanded_qty = int(input("What is the quantity demanded? "))
        
        if demanded_qty <= 0:
            print("Demanded quantity must be a positive integer.")
            return

        for p in products:
            if user_id == int(p["generated_product_id"]):
                current_stock = p["quantity"]
                print(f"\nProduct: {p['name']} | In Stock: {current_stock} | Demanded: {demanded_qty}")
                
                if current_stock >= demanded_qty:
                    print("Status: Stock is OK! You have enough items to fulfill the demand.")
                else:
                    shortage = demanded_qty - current_stock
                    print(f"Status: Insufficient stock! You are short by {shortage} item(s).")
                break
        else:
            print("Product not found.")
            
    except ValueError:
        print("Invalid input. Please enter valid whole numbers for ID and quantity.")

def search_product_by_name():
    print("\n--- SEARCH PRODUCT BY NAME ---")
    search_name = input("Enter the product name to search: ").strip().lower()
    
    found_products = [p for p in products if search_name in p["name"].lower()]
    
    if found_products:
        print(f"\nFound {len(found_products)} product(s) matching '{search_name}':")
        for p in found_products:
            print(p)
    else:
        print(f"No products found matching '{search_name}'.")