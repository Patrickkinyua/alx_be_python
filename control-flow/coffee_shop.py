shop_open = True
if shop_open:
    print("Welcome to the Coffee Shop!")
else:
    print("Sorry, we are closed right now.")

customer_waiting = int(input("How many customers are waiting? "))   

while customer_waiting < 0:
    print("Invalid number of customers. Please enter a non-negative number.")
    customer_waiting = int(input("How many customers are waiting? "))

customer_waiting = customer_waiting
print(f"customer to be served  {customer_waiting} ")

total_served = 0
total_drinks = 0
customer_number = 1

while customer_waiting > 0:
    print(f"Serving customer {customer_number}...")
    drinks = int(input(f"How many drinks does customer {customer_number} want? "))
    while drinks < 0:
        print("Invalid number of drinks. Please enter a non-negative number.")
        drinks = int(input(f"How many drinks does customer {customer_number} want? "))

    drinks_to_prepare = drinks
    drinks_for_customer = 0
    customer_subtotal = 0.0
    receipt_items = []  # Store each drink's details for receipt

    while drinks_to_prepare > 0:
        print(f"Preparing drink {drinks_for_customer + 1} for customer {customer_number}...")
        order = input("enter the item coffee/tea/smoothie: ").lower()
        while order not in ["coffee", "tea", "smoothie"]:
            print("Invalid item. Please enter coffee, tea, or smoothie.")
            order = input("enter the item coffee/tea/smoothie: ").lower()

        size = input("Choose a size (small/medium/large): ").lower()
        while size not in ["small", "medium", "large"]:
            print("Invalid size. Please enter small, medium, or large.")
            size = input("Choose a size (small/medium/large): ").lower()

        size_prices = {"small": 2.00, "medium": 2.50, "large": 3.00}
        price = size_prices[size]
        customer_subtotal += price
        print(f"{order.title()} ({size}) prepared for customer {customer_number}. Price: ${price:.2f}")
        receipt_items.append({"drink": order.title(), "size": size, "price": price})
        drinks_for_customer += 1
        drinks_to_prepare -= 1

    # Print receipt for the customer
    print("\n--- Receipt for Customer {} ---".format(customer_number))
    for idx, item in enumerate(receipt_items, 1):
        print(f"{idx}. {item['drink']} ({item['size']}) - ${item['price']:.2f}")
    print(f"Total: ${customer_subtotal:.2f}")
    print("-----------------------------\n")

    total_served += 1
    total_drinks += drinks_for_customer
    customer_number += 1
    customer_waiting -= 1

print("All customers have been served.")
print(f"Total drinks prepared: {total_drinks}")
print(f"Total revenue: ${customer_subtotal:.2f}")