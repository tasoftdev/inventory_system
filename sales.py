import database
from database import products, sales


def record_sales():
    print("RECORDS")
    try:
        user_id = int(input("What is the generated_product_id? "))
        if user_id <= 0:
            print("Invalid input. ID must be a positive number.")
            return
        user_quantity = int(input("How many are you getting? "))
        if user_quantity <= 0:
            print("Invalid input. Quantity must be a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    target_product = None
    for p in products:
        if p["generated_product_id"] == user_id:
            target_product = p
            break

    if not target_product:
        print("Product not found")
        return

    if target_product["quantity"] < user_quantity:
        print("Out of Stock")
        return

    target_product["quantity"] -= user_quantity
    total_price = target_product["price"] * user_quantity

    transaction = {
        "transaction_id": len(sales) + 1,
        "product_name": target_product["name"],
        "quantity_sold": user_quantity,
        "unit_price": target_product["price"],
        "total_amount": total_price
    }
    
    sales.append(transaction)
    database.save_data()
    print("Successful Transaction")

def view_sales():
    print("VIEW SALES")
    if len(sales) == 0:
        print("We made no sales")
    else:
        print("Congrats on today's sales")
        for i in sales:
            print(i)

def sales_report():
    print("SALES REPORT")
    if len(sales) == 0:
        print("No sales to report")
    else:
        total_sales = sum(sale["total_amount"] for sale in sales)
        print(f"Total Sales Amount: {total_sales}")
        for sale in sales:
            print(sale)