"""
class car:
    name = "premio"
    color = "white"
    def start():
        print("Starting the engine")
        print("Name of the car:", car.name)
        print("color:", car.color)
        car.start()"""


def add(a, b): 
    return a + b 
def sub(a, b): 
    return a - b 
def mul(a, b): 
    return a * b 
def div(a, b): 
    return a / b 
def exp(a, b): 
    return a ** b 
def fdiv(a, b) :
    return a // b 
def mod(a , b): 
    return a 

def claculator(): 
    print("Welcome to our claculator")
chose = input("Enter your chose(1.add/2.sub/3.mul/4.div/5.exp/6.fdiv/7.mod):  ")
if chose in ['1', '2', '3', '4', '5', '6', '7']: 
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))

if chose == '1': 
    result = add(num1, num2)
    print(f"{num1} + {num2} = {result} ")
elif chose == '2': 
    result = sub(num1, num2) 
    print(f"{num1} - {num2} = {result}") 
elif chose == '3': 
    result = mul(num1, num2)
    print(f"{num1} * {num2} = {result}")
elif chose == '4': 
    result = div(num1, num2)
    print(f"{num1} / {num2} =  {result}")
elif chose == '5': 
    result = exp(num1, num2)
    print(f"{num1} ** {num2} = {result}")
elif chose == '6': 
    result = fdiv(num1, num2)
    print(f"{num1} // {num2} = {result} ") 
elif chose == '7': 
    result = mod(num1, num2)
    print(f"{num1} % {num2} = {result}")