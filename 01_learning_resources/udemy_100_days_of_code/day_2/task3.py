# Day 2 of 100 Days of Code Practice File - Mathematical Operations, Order of Operations, Number Manipulation, and F Strings

# Mathematical Operations
print(6 + 3) # Addition
print(6 - 3) # Subtraction
print(6 * 3) # Multiplication  
print(6 / 3) # Division - always results in a float
print(6 // 5) # Always results in an integer by rounding down the result to the nearest whole number, it simply drops all the decimal places and gives you the whole number part of the result so be careful!
print(6 ** 3) # Exponent - raises the first number to the power of the second number
print(6 % 4) # Modulo - gives you the remainder of the division of the first number by the second number

# Order of Operations - Parentheses, Exponents, Multiplication and Division (from left to right), Addition and Subtraction (from left to right)
#PEMDAS or PEMDDALR (to include left to right for multiplication and division, addition and subtraction)
(print(3 * 3 + 3 / 3 - 3)) # This will follow the order of operations to calculate the result

# Rounding function - rounds a number down to the nearest whole number)
print(round(6.5)) # This will round 6.5 down to 6
print(round(6.3)) # This will round 6.3 down to 6
print(round(6.7)) # This will round 6.7 down up to 7

# Number of digits you want to round to - you can specify the number of digits you want to round to by adding a second argument to the round() function
print(round(6.56789, 2)) 
print(round(6.56789, 3)) 

# Number Manipulation

score = 0

# Calculate the score
score += 1 # Score = score + 1
print(score)

score -= 1 # Score = score - 1
print(score)

score *= 1 # Score = score * 2
print(score)

score /= 2 # Score = score / 2
print(score)


# f-Strings allow you to insert a variable/expression into a string without having to use concatenation and type conversion
name = "Alice"
age = 30
score = 0

print(f"{name} is {age} years old and has a score of {score}.")

