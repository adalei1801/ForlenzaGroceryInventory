def add_item(inventory, name, price, quantity):
    """
    Add a new item to the inventory.
    
    Args:
    inventory (dict): The current inventory
    name (str): The name of the item
    price (str): The price of the item
    quantity (str): The quantity of the item
    """

    inventory[name] = {"price": price, "quantity": quantity}
    print(f"{name} added to the inventory.")

            

def remove_item(inventory, name):
    """
    Remove an item from the inventory.
    
    Args:
    inventory (dict): The current inventory
    item_name (str): The name of the item to remove
    """



    del inventory[name]
    print(f"{name} removed from the inventory.")

def update_name(inventory, name, new_name):
    """
    Updates item name from the inventory

    Args:
    inventory (dict): The current inventory
    name (str): The name of the item to be updated
    new_name (str): The new name of the item
    """
    inventory[new_name] = inventory[name]
    print(f"{name} changed to {new_name}.")
    del inventory[name]

def update_quantity(inventory, name, quantity):
    """
    Update the quantity of an item in the inventory.
    
    Args:
    inventory (dict): The current inventory
    name (str): The name of the item to update
    quantity (str): The new quantity of the item
    """

    inventory[name]["quantity"] = quantity
    # Ticket #2: Changed double equal to single to assign new quantity
    print(f"\n{name} quantity updated to {quantity}.")

def update_price(inventory, name, price):
    """
    Update the price of an item in the inventory

    Args:
    inventory (dict): The current inventory
    name (str): The name of the item to update
    price(float): The new price of the item
    """

    inventory[name]["price"] = price
    print(f"\n{name} price changed to ${price:.2f}.")

def display_inventory(inventory):
    """
    Display all items in the inventory.
    
    Args:
    inventory (dict): The current inventory
    """
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for name in inventory:
            item = inventory[name]

            if item["quantity"] == "0":
                 print(f"[SOLD OUT] {name}: Price: ${item['price']:.2f}, Quantity: {item['quantity']}")
            else:
                print(f"{name}: Price: ${item['price']:.2f}, Quantity: {item['quantity']}")
            # Ticket #1: Changing item to name fixes formatting issue and allows items to be removed smoothly


# Initialize inventory with two example items
inventory = {
    "apple": {"price": 0.50, "quantity": 100},
    "banana": {"price": 0.75, "quantity": 150}
}

while True:
    display_inventory(inventory)
    # Ticket #4: Prints inventory at the start of every loop by calling the display inventory function 
    print("\nOptions: ")
    print("1. Add item\n2. Remove item\n3. Update items\n4. Exit")
    choice = input("What would you like to do? Enter your choice (1-5): ")


    # Add item
    if choice == "1":
        name = input("Enter item name: ")
        if name in inventory:
            overwrite = input("This item already exists, do you want to overwrite it? Yes or no? ")
            if overwrite == "yes":
                price = float(input("Enter item price: "))
                quantity = int(input("Enter item quantity: "))
                add_item(inventory, name, price, quantity)
                continue
            elif overwrite == "no":
                continue
        # Ticket #3: Checks if item already exists and if the user wants to overwrite it, if so, the item is overwritten.
    
        price = float(input("Enter item price: "))
        # Ticket #3: Making input a float solves formatting issue
        quantity = int(input("Enter item quantity: "))
        add_item(inventory, name, price, quantity)

    # Remove item
    elif choice == "2":
        name = input("Enter item name to remove: ")

        while name not in inventory:
            print("\nItem not in inventory, try again ")
            name = input("Re-enter item name: ")

        remove_item(inventory, name)

    elif choice == "3":
        print("\nUpdate Item Menu:")
        print("1. Name\n2. Price\n3. Quantity\n4. Back to Home")
        item_choice = input("What do you want to update. Enter choice (1-4): ")

        if item_choice == "1":
            name = input("Enter item name to update: ")

            while name not in inventory:
                print("\nItem not in inventory, try again ")
                name = input("Re-enter item name: ")

            new_name = input("Enter new name: ")
            update_name(inventory, name, new_name)

        elif item_choice == "2":
            name = input("Enter name of item: ")

            while name not in inventory:
                print("\nItem not in inventory, try again ")
                name = input("Re-enter item name: ")

            price = float(input("Enter new price: "))
            update_price(inventory, name, price)

        elif item_choice == "3":
            name = input("Enter item name to update: ")

            while name not in inventory:
                print("\nItem not in inventory, try again ")
                name = input("Re-enter item name: ")
            
            quantity = input("Enter new quantity: ")

            if quantity == "0":
                to_rev = input("This item's quantity is 0, would you like to remove it from the inventory? Yes or no? ")
                if to_rev == "yes":
                    remove_item(inventory, name)
        
            update_quantity(inventory, name, quantity)

        elif item_choice == "4":
            print("\nReturning to Home")
            continue

    # Exit program
    elif choice == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")