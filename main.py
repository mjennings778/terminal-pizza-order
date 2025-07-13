pizzas = ["Meatlovers", "Vegetarian", "Aussie", "Mexicana", "Margherita", "Neapolitan"]
sizes = ["small", "medium", "large", "family"]
base_cost = 10
medium_cost = base_cost * 0.2
large_cost = base_cost * 2
family_cost = base_cost * 3
print("Thank you for calling Pepe's Pizza Store. How many I help you?")
print("1. Delivery")
print("2. Pickup")

user_choice = int(input("Enter either option 1 or 2: "))

if user_choice == 1:
    print("May I start with your name, phone number and address?")
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")
    print("What can I get for you today?")
    for item in pizzas:
        print(item)
    user_pizza_choice = input("I would like: ")
    if user_pizza_choice in pizzas:
        pass
    while not user_pizza_choice in pizzas:
        print(f"'{user_pizza_choice}' is not on our menu")
        print("What can I get for you today?")
        user_pizza_choice = input("I would like: ")

    print("What size were you after?")
    for item in sizes:
        print(item)
    user_pizza_size_choice = input("I would like: ")
    if user_pizza_size_choice in sizes:
        pass
    while not user_pizza_size_choice in sizes:
        print(f"'{user_pizza_size_choice}' is not on our menu")
        print("What size were you after?")
        user_pizza_size_choice = input("I would like: ")
    if user_pizza_size_choice == "small":
        print(f"The total for your order will be ${base_cost}")
    if user_pizza_size_choice == "medium":
        print(f"The total for your order will be ${medium_cost}")
    if user_pizza_size_choice == "large":
        print(f"The total for your order will be ${large_cost}")
    if user_pizza_size_choice == "family":
        print(f"The total for your order will be ${family_cost}")