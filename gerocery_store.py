import csv
import os

def manage_grocery_data(filename, data=None, mode='read'):
    # 1. Create file with headers ONLY if it doesn't exist
    if not os.path.exists(filename):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Item Name', 'Price', 'Quantity'])

    # 2. Writing Logic
    if mode == 'write' and data:
        with open(filename, 'a', newline='') as f:
            writer = csv.writer(f)
            # Ensure data is a list/tuple before writing
            writer.writerow(data if isinstance(data, (list, tuple)) else [data])
            print(f"Successfully added: {data}")

    # 3. Reading Logic
    elif mode == 'read':
        print(f"\n--- Current Inventory ({filename}) ---")
        try:
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    # Added a check to handle empty rows if any
                    if row:
                        print(f"{row[0]:<15} | {row[1]:<10} | {row[2]:<10}")
        except FileNotFoundError:
            print("File not found.")

# Define the filename once to avoid typos
DB_FILE = "grocery_items.csv"

print("############ Welcome to Shantoo Grocery Store ############")
print("Are you 'Staff' or 'Customer'?")
first_message = input("Select 1 for Staff, 2 for Customer: ")

if first_message == '1':
    try:
        print("R for Retrieve, U for Update, or C for Create Entry")
        staff_message = input("Enter R, U or C: ").upper()
        
        if staff_message == 'R':
            manage_grocery_data(DB_FILE, mode='read')
        elif staff_message == 'C':
            item = input("Item Name: ")
            price = input("Price: ")
            qty = input("Quantity: ")
            manage_grocery_data(DB_FILE, data=[item, price, qty], mode='write')
        elif staff_message == 'U':
            
            print("Update feature coming soon!")
            
    except Exception as e:
        print(f"An error occurred: {e}")