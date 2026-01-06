grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}
# 2 check and update Price
#grocery_inventory.get("Eggs")
print("Details of Eggs:", grocery_inventory.get("Eggs"))
if grocery_inventory["Eggs"] [1] > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    category, old_price, stock = grocery_inventory["Eggs"]
    new_price = old_price - 1
    grocery_inventory["Eggs"] = (category, new_price, stock)
    print("Updated Eggs details:", grocery_inventory["Eggs"])
else:
    print("The price of Eggs is reasonable.")
#3 Add new item
grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)
print("Inventory after adding Tomatoes:", grocery_inventory)
#4 Manage Stock
grocery_inventory.get("Milk")[2]
print("Milk stock:", grocery_inventory.get("Milk")[2])
if grocery_inventory["Milk"] [2] < 10:
    print("Milk needs to be restocked. Increasing Stock by 20 units.")
    category, price, old_stock = grocery_inventory["Milk"]
    new_stock = old_stock + 20
    grocery_inventory["Milk"] = (category, price, new_stock)
    print("Milk stock update:", grocery_inventory["Milk"])
else:
    print("Milk has sufficient stock.")

#5 Remove item based on price
if grocery_inventory["Apples"][1] > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

print("Updated inventory:", grocery_inventory)

