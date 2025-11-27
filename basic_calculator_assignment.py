# ----------------------------------------------------------------------------------------
#                          ASSIGNMENT PROJECT
#                                   ON
#                "OBJECT-ORIENTED MENU-DRIVEN CALCULATOR"
# ----------------------------------------------------------------------------------------

#           Project Title                : SmartCalc OOP
#           Module 5 Assignment Topic    : Object-Oriented Menu-Driven Calculator
#           Course Name                  : Full Stack Web Development with Python, Django & React
#           Batch                        : 8
#           Institution Name             : OSTAD

#           This project covers:
#           ✔ Arithmetic functions (add, subtract, multiply, divide)
#           ✔ User input handling
#           ✔ Input validation using try–except
#           ✔ Menu-driven calculator system
#           ✔ Object-Oriented Calculator class design
#           ✔ Looping until Exit (menu keeps running)
#           ✔ Division-by-zero protection
# ----------------------------------------------------------------------------------------

#                          ASSIGNMENT SUBMISSION
#                        --------------------------

#                             Submitted To
#                           -----------------
#                            OSTAD Instructor

#                             Submitted By
#                          -------------------
#                       Name: Md. Ahosanul Kabir
#                       Phone: 01762007433
#                       Email: akl279f@gmail.com

#                    Submission Date: 28 November, 2025
# ----------------------------------------------------------------------------------------




# -----------------------------
#    Arithmetic Functions
# -----------------------------

def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract_numbers(a, b):
    """Return the subtraction of two numbers."""
    return a - b


def multiply_numbers(a, b):
    """Return the product of two numbers."""
    return a * b


def divide_numbers(a, b):
    """Safely divide two numbers."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


# -----------------------------
#    Input Validation Function
# -----------------------------

def get_valid_number(prompt):
    """Ask the user for a number until valid input is entered."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")


# -------------------------------------------------------
#    OBJECT-ORIENTED PROGRAM: Calculator Class
# -------------------------------------------------------

class Calculator:

    # ----- Arithmetic Methods -----
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero."
        return a / b

    # ----- Menu Method -----
    def menu(self):
        print("\n==============================")
        print("     SmartCalc OOP")
        print("==============================")
        print("Press 1. Add")
        print("Press 2. Subtract")
        print("Press 3. Multiply")
        print("Press 4. Divide")
        print("Press 5. Exit")
        print("=" * 40)

    # ----- Run Method -----
    def run(self):
        while True:
            self.menu()
            choice = input("Enter your choice (1–5): ")

            if choice == '5':
                print("\nThank you for using the calculator!")
                break

            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice! Please enter a number between 1 and 5.")
                continue

            # Get two validated numbers
            num1 = get_valid_number("Enter first number: ")
            num2 = get_valid_number("Enter second number: ")

            # Perform selected operation
            if choice == '1':
                result = self.add(num1, num2)
                print(f"\nResult: {num1} + {num2} = {result}")

            elif choice == '2':
                result = self.subtract(num1, num2)
                print(f"\nResult: {num1} - {num2} = {result}")

            elif choice == '3':
                result = self.multiply(num1, num2)
                print(f"\nResult: {num1} × {num2} = {result}")

            elif choice == '4':
                result = self.divide(num1, num2)
                print(f"\nResult: {num1} ÷ {num2} = {result}")

            print("\n-----------------------------------")


# -------------------------------------------------------
#    Creation of Calculator Object and Start Program
# -------------------------------------------------------
if __name__ == "__main__":
    calc = Calculator()
    calc.run()
