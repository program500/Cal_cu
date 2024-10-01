def addition(a, b):
    return a + b 
def subtraction(a, b):
    return a - b 
def multiplication(a, b):
    return a * b 
def division(a, b):
    return a / b 
def modulus(a, b):
    return a % b 

def calculator():
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.modulus")
choice = input("Enter your choice (1.addition/2.subtraction/3.multiplication/4.division/5.modulus):  ")

if choice in['1', '2', '3', '4', '5']:
    try:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        if choice == '1':
          result = addition(num1, num2)
          print(f"{num1} + {num2} = {result} ")
        elif choice == '2': 
            result = subtraction(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = multiplication(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == '4': 
            result = division(num1, num2)
            print(f"{num1} / {num2} = {result}")
        elif choice == '5':
            result = modulus(num1, num2)
            print(f"{num1} % {num2} = {result}")
                  
    except ValueError:
        print("Error: Invalid input. Please enter numerical values.")
    else:
        print("Error: Invalid choice. Please select a valid operation.")


# Run the calculator
if __name__ == "__main__":
    calculator()


print("Thanks for practice our ")

