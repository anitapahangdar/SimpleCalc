"""A small, reusable command-line calculator by Anita Pahangdar."""


def calculate(first_number, second_number, operation):
    """Return the result of applying an arithmetic operation."""
    if operation == "+":
        return first_number + second_number
    if operation == "-":
        return first_number - second_number
    if operation == "*":
        return first_number * second_number
    if operation == "/":
        if second_number == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return first_number / second_number
    raise ValueError("Choose one of: +, -, *, /.")


def read_number(prompt):
    """Prompt until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    """Run the interactive calculator loop."""
    print("SimpleCalc — enter an operation or type 'exit' to quit.")

    while True:
        operation = input("\nOperation (+, -, *, /, exit): ").strip().lower()
        if operation == "exit":
            print("Goodbye!")
            break
        if operation not in {"+", "-", "*", "/"}:
            print("Choose one of: +, -, *, /, or exit.")
            continue

        first_number = read_number("Enter the first number: ")
        second_number = read_number("Enter the second number: ")

        try:
            result = calculate(first_number, second_number, operation)
            print(f"Result: {result:g}")
        except ZeroDivisionError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
