# Day 3 of 100 Days of Code Practice File - logical operators

# Using logical operators to give those who are experiencing a midlife crisis (ages 45-55) a free rollercoaster ticket

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
    elif age >= 45 and age <= 55:
        print("Congratulations! You get a free rollercoaster ticket since you are in the midlife crisis state of life! :-D")
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
    