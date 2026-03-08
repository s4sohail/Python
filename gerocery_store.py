import csv
import os

def manage_grocery_data(filename, data=None, mode='read'):
    # 1. Create file with headers if it doesn't exist
    if not os.path.exists(filename):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Item Name', 'Price', 'Quantity'])

    # 2. Reading Logic (with Row Numbers)
    if mode == 'read':
        print(f"\n{'ID':<5} | {'Item Name':<15} | {'Price':<10} | {'Quantity':<10}")
        print("-" * 45)
        try:
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                next(reader)  # Skip header
                for i, row in enumerate(reader, start=1):
                    if row:
                        print(f"{i:<5} | {row[0]:<15} | {row[1]:<10} | {row[2]:<10}")
        except FileNotFoundError:
            print("File not found.")

    # 3. Writing Logic (with Duplicate Check)
    elif mode == 'write' and data:
        current_items = []
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            current_items = [row[0].lower() for row in reader if row]

        if data[0].lower() in current_items:
            print(f"Error: '{data[0]}' already exists in inventory!")
        else:
            with open(filename, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(data)
                print(f"Successfully added: {data}")

    # 4. Update Logic (Row Number Based)
    elif mode == 'update':
        rows = []
        with open(filename, 'r') as f:
            rows = list(csv.reader(f))

        manage_grocery_data(filename, mode='read') # Show list first
        try:
            row_idx = int(input("\nEnter Row ID to update: "))
            # Check if index is valid (skip header at index 0)
            if 0 < row_idx < len(rows):
                print(f"Updating: {rows[row_idx]}")
                new_item = input("New Item Name (leave blank to keep): ") or rows[row_idx][0]
                new_price = input("New Price (leave blank to keep): ") or rows[row_idx][1]
                new_qty = input("New Quantity (leave blank to keep): ") or rows[row_idx][2]
                
                rows[row_idx] = [new_item, new_price, new_qty]
                
                with open(filename, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(rows)
                print("Update successful!")
            else:
                print("Invalid Row ID.")
        except ValueError:
            print("Please enter a valid number.")

    elif mode == 'delete':
        rows = []
        with open(filename, 'r') as f:
            rows = list(csv.reader(f))

        manage_grocery_data(filename, mode='read') # Show list first
        try:
            row_idx = int(input("\nEnter Row ID to update: "))
            # Check if index is valid (skip header at index 0)
            if 0 < row_idx < len(rows):
                print(f"Deleteing: {rows[row_idx]}")
                del(rows[row_idx])
            
                with open(filename, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(rows)
                print("Update successful!")
            else:
                print("Invalid Row ID.")
        except ValueError:
            print("Please enter a valid number.")

# --- Main App ---
DB_FILE = "grocery_items.csv"
print("############ Welcome to Shantoo Grocery Store ############")
choice = input("Select 1 for Staff, 2 for Customer: ")

if choice == '1':
    print("R for Retrieve, U for Update, D for Delete, or C for Create Entry")

    for i in range(5):
        action = input("Enter R, U, D or C (Exit -> E): ").upper()
            
        if action == 'R':
            manage_grocery_data(DB_FILE, mode='read')
        elif action == 'C':
            item = input("Item Name: ")
            price = input("Price: ")
            qty = input("Quantity: ")
            manage_grocery_data(DB_FILE, data=[item, price, qty], mode='write')
        elif action == 'U':
            manage_grocery_data(DB_FILE, mode='update')
        elif action == 'D':
            manage_grocery_data(DB_FILE, mode='delete')
        elif action == 'E':
            
            print("Thank you for using Grocery software")
            break

elif choice =='2':
    print("Customer Part will coming soon")