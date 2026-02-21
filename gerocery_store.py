import csv
import os

def manage_grocery_data(filename, data=None, mode='read'):
    """
    Handles basic CSV operations for the grocery store.
    :param filename: Name of the csv file (e.g., 'inventory.csv')
    :param data: A list of values to write [Item, Price, Quantity]
    :param mode: 'write' to add data, 'read' to display data
    """
    
    # Ensure the file exists with headers if it's new
    if not os.path.exists(filename):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Item Name', 'Price', 'Quantity'])

    if mode == 'write' and data:
        with open(filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
            print(f"Successfully added: {data}")

    elif mode == 'read':
        print(f"\n--- Current Inventory ({filename}) ---")
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                print(f"{row[0]:<15} | {row[1]:<10} | {row[2]:<10}")


manage_grocery_data("grocery_items.csv", "this is test data", "read")

# print("############ Welcome to Shantoo Grocery Store ############")
# print("Are you! 'Staff' or 'Customer' ?")
# first_message = input("Select 1 for Staff 2 for Customer: ")

# print(first_message)

# if first_message == '1':
#     print("R for retrieve and U for update or C for Create Inventry")
#     staff_message = input("Enter R , U or C: ")
#     if staff_message.capitalize() == 'R':
#         manage_grocery_data('gerocery_items.csv')
#     elif staff_message.capitalize() == 'U':
         
    