print("Welcome to the Basic Math Operations Program")

#Inputs
#First variable
while True:
    try:
        # Prompt the user to enter the first number and convert it to a float
        num1 = float(input("Enter the first number:"))
        #If the conversion is successful, exit the loop.

        break
    except ValueError:
        #If a ValueError occurs (e.g., the user enters a non-numeric value), print an error message and prompt the user again.
        print("Invalid input. Please enter a valid number.")

#Second variable
while True:
    try:
        # Prompt the user to enter the second number and convert it to a float
        num2 = float(input("Enter the second number:"))
        #If the conversion is successful, check if it's not zero to avoid division by zero error.
        if num2 == 0:
            print("The second number cannot be zero to avoid the division by zero error. Please enter a non-zero number.")
        else:
            break
    except ValueError:
        #If a ValueError occurs (e.g., the user enters a non-numeric value), print an error message and prompt the user again.
        print("Invalid input. Please enter a valid number.")       
#Performing basic math operations
print(f"The sum of {num1} and {num2} is: {num1 + num2:.2f}")
print(f"The difference between {num1} and {num2} is: {num1 - num2:.2f}")
print(f"The product of {num1} and {num2} is: {num1 * num2:.2f}")
print(f"The quotient of {num1} divided by {num2} is: {num1 / num2:.2f}")
