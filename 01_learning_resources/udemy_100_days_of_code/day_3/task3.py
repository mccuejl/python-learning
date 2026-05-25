# Day 3 of 100 Days of Code Practice File - nested if/elif statements, multiple if statement in succession

# Condition check with if/else
print("Welcome to the world's fastest rollercoaster!")
height = int(input("What is your height in inches? "))
bill = 0

if height >= 48:
    print("You are tall enough to ride the rollercoaster!🎉")
    age = int(input("How old are you? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.") 

    wants_photo = input("Do you want to purchase a photo of your ride? Type y for Yes and n for No. ")
    if wants_photo == "y": 
        # Add $3 to their bill for the purchase of a photo
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you are not tall enough. Please come back when you are taller to ride the rollercoaster!")
    
    