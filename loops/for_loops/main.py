# Each product has a list with current stock as the first item 
# and minimum stock as the second item
inventory = {
    "Milk": [25, 20],
    "Eggs": [250, 200],
    "Bread": [30, 50],  # This item needs restocking
    "Apples": [50, 45]
}

# Promotions dictionary
promotions = {
    "Eggs": "20% off",
    "Apples": "Buy one, get one free"
}

# Task 1: Complete the for loop to iterate through the `inventory` dictionary
for item in inventory:
    # Print the current item 
    print(f"--- Processing: {item} ---")

    # Task 2: Access the current stock and minimum stock for each product
    current_stock = inventory[item][0]  # Access current stock
    min_stock = inventory[item][1]  # Access minimum stock
    
    # Task 3: Write a condition to check if current stock is less than or equal to minimum stock
    if current_stock <= min_stock:
        # If the stock is too low, print a message indicating the need for restocking
        print(f"{item} needs restocking. Current stock: {current_stock}. Minimum required: {min_stock}")
        
        # Task 4: Increase the current stock by 20 units and update the inventory
        inventory[item][0] = current_stock + 20
        
        # Print the updated stock level for the item
        print(f"Updated stock for {item}: {inventory[item][0]}")

    # Task 5: Complete the condition to check if the product has a promotion
    if item in promotions:
        # If a promotion exists, print the promotion details
        print(f"Promotion for {item}: {promotions[item]}")
    else:
        # If no promotion exists, print a message indicating that there is no promotion
        print(f"No promotions for {item}")