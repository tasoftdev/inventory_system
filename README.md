# 📦 Inventory Management System (IMS)

A robust, console-based Inventory Management and Sales Tracking System built in Python. It features automated file persistence using JSON, dynamic product ID re-indexing, and comprehensive sales reporting.

---

## ✨ Key Features

* **Product Management:** Add, view, update, and delete products with strict input validation (ensuring non-empty names/categories, positive prices, and whole number quantities).
* **Smart ID Sequencing & Re-indexing:** Automatically generates sequential IDs starting from `1`. When a product is deleted, remaining products automatically shift down and re-index sequentially to avoid gaps.
* **Stock & Sales Control:** Check stock availability against customer demand, record sales transactions, and automatically deduct purchased quantities from your live inventory.
* **Search Functionality:** Search for products dynamically by name (case-insensitive substring matching).
* **Sales Tracking & Reporting:** View historical transactions and generate automated financial sales reports showing total revenue and itemized logs.
* **Persistent Storage:** Automatically saves and loads your inventory and sales data using local JSON files (`products.json` and `sales.json`).

---

## 📂 Project Structure

```text
InventoryManagementSystem/
│
├── database.py       # Handles JSON data loading and file persistence
├── products.py       # Product management, search, and stock checking logic
├── sales.py          # Sales recording, viewing, and financial reporting logic
├── main.py           # Main control loop, menu navigation, and program entry point
├── products.json     # Local database file storing products (auto-generated)
└── sales.json        # Local database file storing sales transactions (auto-generated)