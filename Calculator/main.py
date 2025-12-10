from art import logo

def perform_operation(n1, operation, n2):
    result = 0
    if operation == "+":
        result = n1 + n2
    elif operation == "-":
        result = n1 - n2
    elif operation == "*":
        result = n1 * n2
    elif operation == "/":
        result = n1 / n2
    print(f"{n1} {operation} {n2} = {result}")
    return result

def get_number(prompt: str) -> float:
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number.")

def get_operation() -> str:
    operations = ["+", "-", "*", "/"]
    print("+\n-\n*\n/")
    while True:
        op = input("Pick an operation: ")
        if op in operations:
            return op
        print("Invalid operation. Try again.")

def perform_calculation(first_number: int = None):
    if first_number is None:
        first_number = get_number("What's the first number?: ")
    operation = get_operation()
    second_number = get_number("What's the second number? ")
    result = perform_operation(first_number, operation, second_number)
    return result


def main() -> None:
    print(logo)
    memory_number = None
    user_choice = "n"
    while True:
        result = 0
        if user_choice == "n":
            result = perform_calculation()
        elif user_choice == "y":
            result = perform_calculation(memory_number)

        user_choice = input("Type 'y' to continue or type 'n' to start new calculation. Type 'c' to finish: ")
        if user_choice == "y":
            memory_number = result
        elif user_choice == "c":
            break

if __name__ == "__main__":
    main()
