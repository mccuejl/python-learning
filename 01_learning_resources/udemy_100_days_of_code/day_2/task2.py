# Day 2 of 100 Days of Code Practice File - Type Error, Type Checking, and Type Conversion

# Type Error
# len(12345) # Won't work - Type Error because len() function only works with strings, lists, tuples, etc. but not with integers
# print(len("12345")) # This works because it's a string

# Type Checking - to check the data type of a value
# print(type("Hello")) #Integer
# print(type(123)) # String
# print(type(9.99)) # Float
# print(type(True)) # Boolean

# Type Conversion - to convert one data type to another
# print(int("567") + (float("9.99"))) # Convert string "567" to an integer and string "9.99" to a float, then add them together

# Print the number of letters in users name using type conversion
name_of_the_user = input("What is your name? ")
name_length = len(name_of_the_user)
print("Your name has " + str(name_length) + " letters.")
