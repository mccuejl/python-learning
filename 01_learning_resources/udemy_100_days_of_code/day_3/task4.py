# Day 3 of 100 Days of Code Practice File - code challenge #2

# Calculate total amount due for customer's pizza order

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want: S, M, or L? ")
pepperoni = input("Do you want pepperoni on your pizza: Y or N?")
extra_cheese = input("Do you want to add extra cheese? Y or N: ")

# Calculate how much they need to pay based on the size of their choice
pizza_cost = 0
if size == "S":
    pizza_cost += 5
    print(f"Small pizzas are ${pizza_cost}.")
elif size == "M":
    pizza_cost += 20
    print(f"Medium pizzas are ${pizza_cost}.")
elif size == "L":
    pizza_cost += 25
    print(f"Large pizzas are ${pizza_cost}.")
else:
    print("Error: That is not a valid pizza size.")

# Add pepperoni charge to bill
if pepperoni == "Y":
    if size == "S":
        pizza_cost += 2
    else:
        pizza_cost += 3

# Add extra cheese charge to bill
if extra_cheese == "Y":
    pizza_cost += 1

print(f"Your final bill is ${pizza_cost}.")
