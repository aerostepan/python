menu = {"pizza": 3.00,
        "burger": 2.50,
        "salad": 2.00,
        "fries": 1.50,
        "popcorn": 6.00,
        "chips": 1.00,
        "soda": 0.99}

cart = []
total = 0

print("-----Menu-----")
for key, value in menu.items():
    print(f"{key:10}: €{value:.2f}")
print("--------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:    
        cart.append(food)

print("--------Your Order-------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: €{total:.2f}")
