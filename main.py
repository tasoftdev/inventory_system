import database
from products import check_stock_availability, search_product_by_name
from products import add_products, view_products, update_products, delete_products
from sales import record_sales, view_sales, sales_report

def display_main_menu():
    print("="*40)
    print(" MAIN MENU ")
    print("="*40)
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product")
    print("4. Record Sale")
    print("5. Delete Product")
    print("6. View Sales")
    print("7. Check Stock Availability")
    print("8. Search Product")
    print("9. Sales Report")
    print("10. Exit")
    print()
    print("="*40)

database.load_data()

while True:
    display_main_menu()
    choice = input("Enter your choice (1-10): ")
    if choice == "1":
        add_products()
    elif choice == "2":
        view_products()
    elif choice == "3":
        update_products()
    elif choice == "4":
        record_sales()
    elif choice == "5":
        delete_products()
    elif choice == "6":
        view_sales()
    elif choice == "7":
        check_stock_availability()
    elif choice == "8":
        search_product_by_name()
    elif choice == "9":
        sales_report()
    elif choice == "10":
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice. Please try again.")
try:
    display_main_menu()
except KeyboardInterrupt:
    print("\nProgram interrupted. Exiting...")
    
database.save_data()
print("Data saved successfully. Exiting the program.")

def display_header():
    print("="*40)
    print(" Inventory Management System ")
    print("="*40)
    print("Welcome!")

display_header()
