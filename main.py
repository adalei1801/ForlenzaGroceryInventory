def add_item(inventory, name, price, quantity):
    """
    Add a new item to the inventory.
    
    Args:
    inventory (dict): The current inventory
    name (str): The name of the item
    price (str): The price of the item
    quantity (str): The quantity of the item
    """
    if name in inventory:
        overwrite = input("This item already exists, do you want to overwrite it? Yes or no? ")
        if overwrite == "yes":
            inventory[name] = {"price": price, "quantity": quantity}
            print(f"{name} added to the inventory.")

    # Ticket #3: Checks if item already exists and if the user wants to overwrite it, if so, the item is overwritten.

            

def remove_item(inventory, name):
    """
    Remove an item from the inventory.
    
    Args:
    inventory (dict): The current inventory
    item_name (str): The name of the item to remove
    """
    del inventory[name]
    print(f"{name} removed from the inventory.")

def update_quantity(inventory, name, quantity):
    """
    Update the quantity of an item in the inventory.
    
    Args:
    inventory (dict): The current inventory
    item_name (str): The name of the item to update
    new_quantity (str): The new quantity of the item
    """
    inventory[name]["quantity"] = quantity
    # Ticket #2: Changed double equal to single to assign new quantity
    print(f"{name} quantity updated to {quantity}.")

def display_inventory(inventory):
    """
    Display all items in the inventory.
    
    Args:
    inventory (dict): The current inventory
    """
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        print("Current Inventory:")
        for name in inventory:
            item = inventory[name]
            print(f"{name}: Price: ${item['price']:.2f}, Quantity: {item['quantity']}")
            # Ticket #1: Changing item to name fixes formatting issue and allows items to be removed smoothly

# Initialize inventory with two example items
inventory = {
    "apple": {"price": 0.50, "quantity": 100},
    "banana": {"price": 0.75, "quantity": 150}
}

while True:
    print("Current Inventory:\n")
    display_inventory(inventory)
    # Ticket #4: Prints inventory at the start of every loop by calling the display inventory function 
    print("\n1. Add item\n2. Remove item\n3. Update quantity\n4. Display inventory\n5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter item name: ")
        price = input("Enter item price: ")
        quantity = int(input("Enter item quantity: "))
        add_item(inventory, name, price, quantity)
    elif choice == "2":
        name = input("Enter item name to remove: ")
        remove_item(inventory, name)
    elif choice == "3":
        name = input("Enter item name to update: ")
        quantity = input("Enter new quantity: ")
        update_quantity(inventory, name, quantity)
    elif choice == "4":
        display_inventory(inventory)
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")