import json  # For saving and loading data as JSON

inventory = {}  # Dictionary to store inventory
file_name = "inventory_data.json"  # The file name to store data

# Load inventory from the file if it exists
def load_inventory():
    global inventory
    try:
        with open(file_name, "r") as file:
            inventory = json.load(file)
            print("✅ Inventory loaded successfully!")
    except FileNotFoundError:
        print("❌ No previous inventory data found. Starting fresh.")
    except json.JSONDecodeError:
        print("❌ Error decoding inventory data. Starting fresh.")

# Save inventory to a file
def save_inventory():
    with open(file_name, "w") as file:
        json.dump(inventory, file, indent=4)
        print("✅ Inventory saved successfully!")

# Add item function (no change)
def add_item(): 
    global inventory
    product_category = input("\n\nEnter product category (e.g., Pen, Book): ")
    product_name = input("Enter product name: ")
    product_quantity = int(input("Enter quantity of the product: "))
    product_price = int(input("Enter price of product: "))
    
    if product_category not in inventory:
        inventory[product_category] = {}
    
    inventory[product_category][product_name] = {
        "Quantity" : product_quantity,
        "Price": product_price 
    }

    print(f"{product_name} added under category '{product_category}' successfully!")
    save_inventory()  # Save inventory to file after adding

# View items function (no change)
def view_items(): 
    global inventory
    for category, products in inventory.items():
        print(f"📦 Category: {category}")
        for product_name, details in products.items():
            print(f"     🖊 Product: {product_name}")
            print(f"     🔢 Quantity: {details['Quantity']}")
            print(f"     💰 Price: {details['Price']}")

# Update stock function (no change)
def update_stock(): 
    global inventory
    update_category_name = input("Enter exact category name of product you want to update: ")
    if(update_category_name in inventory):
        update_product_name = input("Enter exact product name you want to update: ")
        if(update_product_name in inventory[update_category_name]):
            new_quantity = int(input("Enter new quantity: "))
            new_price = int(input("Enter new price: "))

            inventory[update_category_name][update_product_name]['Quantity'] = new_quantity
            inventory[update_category_name][update_product_name]['Price'] = new_price

            print(f"✅ {update_product_name} updated successfully!")
            save_inventory()  # Save inventory to file after update

        else:
            print(f"❌ Product '{update_product_name}' not found in category '{update_category_name}'")

    else:
        print(f"❌ Category '{update_category_name}' not found in inventory")

# Delete item function (no change)
def delete_item():
    global inventory
    delete_category_name = input("Enter exact category name of product you want to delete: ")

    if delete_category_name in inventory:
        delete_product_name = input("Enter exact name of product you want to delete: ")

        if delete_product_name in inventory[delete_category_name]:
            del inventory[delete_category_name][delete_product_name]
            print(f"🗑️ '{delete_product_name}' deleted successfully from '{delete_category_name}'!")

            if not inventory[delete_category_name]:
                del inventory[delete_category_name]
                print(f"📁 Category '{delete_category_name}' is now empty and deleted.")
            save_inventory()  # Save inventory to file after deletion
        else:
            print(f"❌ Product '{delete_product_name}' not found in '{delete_category_name}'!")
    else:
        print(f"❌ Category '{delete_category_name}' not found in inventory!")

# Main loop
while True:
    load_inventory()  # Load the inventory data when the program starts

    print("\n📦 Inventory Management System")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Update Stock")
    print("4. Delete Item")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if(choice == "1"):
        add_item()

    elif(choice == "2"):
        view_items()

    elif(choice == "3"):
        update_stock()

    elif(choice == "4"):
        delete_item()

    elif(choice == "5"):
        print("Exiting the app...")
        break
