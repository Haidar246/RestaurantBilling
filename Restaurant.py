# Super Simple Restaurant Billing System

menu = {"Pizza":150, "Burger":80, "Pasta":120, "Coffee":50}

print("=== Menu ===")
for item, price in menu.items():
    print(f"{item}: ₹{price}")

orders = []
while True:
    item = input("\nEnter item (or 'done'): ").title()
    if item == "Done": break
    if item in menu:
        qty = int(input("Quantity: "))
        orders.append((item, qty, menu[item]*qty))
    else:
        print("Sorry item Not available!")

print("\n=== BILL ===")
total = 0
for i, q, p in orders:
    print(f"{i} x{q} = ₹{p}")
    total += p
print(f"Total: ₹{total}")