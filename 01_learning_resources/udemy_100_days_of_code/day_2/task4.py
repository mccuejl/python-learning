# Day 2 of 100 Days of Code Project File - Tip Calculator

print("Welcome to Jamie's tip calculator!")

# User enters the total amount of the bill before tip
total_bill = float(input("What is the total bill? \n$"))

# User enters the tip percentage they would like to give
tip_percent = int(input("What percentage tip would you like to give to your server? \n"))

# User enters how many people to split the bill between
people_split = int(input("How many people are splitting the bill? \n")) 

# Prints total bill with tip
bill_with_tip = (tip_percent / 100 * total_bill) + total_bill
print(f"The total bill with tip is ${bill_with_tip:.2f}.")

# Calculate and print how much to pay per person
pay_per_person = bill_with_tip / people_split
print(f"Each person should pay ${pay_per_person:.2f}.")
