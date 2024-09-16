# Step 1: Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("+   For addition")
print("-   For subtraction")
print("*   For multiplication")
print("/   For division")

operation = input("Enter the operation (+, -, *, /): ")

# Step 2: Perform the operation based on user input
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation!"

# Step 3: Output the result
print(f"The result is: {result}")
