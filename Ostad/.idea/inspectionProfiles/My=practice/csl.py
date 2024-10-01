def addition(a,b):
    return a + b 
def subtrction(a, b):
    return a - b 
def multiplication(a, b):
    return a * b 
def division(a, b):
    return a / b 
def modulus(a, b):
    return a % b 
def gr(a, b):
    return a > b 
def ls(a, b):
    return a < b 
def gq(a, b):
    return a >= b 
def lq(a, b):
    return a <= b 
def dq(a, b):
    return a == b 
def fd(a, b):
    return a // b 
def expo(a, b ): 
    return a ** b 
def calculator():
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.modulus")
    print("6.gr")
    print("7.ls")
    print("8.gq")
    print("9.lq")
    print("10.dq")
    print("11.fd")
    print("12.expo")
chose = input("Enter chose: (1.add/2.sub/3.mul/4.div/5.modu/6.gr/7.ls/8.gq/9.lq/10.dq/11.fd/12.expo)")

if chose in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    if chose == '1':
        result = addition(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif chose  == '2': 
        result = subtrction(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif chose == '3': 
        result = multiplication(num1 , num2)
        print(f"{num1} * {num2} = {result}")
    elif chose == '4': 
        result = division(num1, num2)
        print(f"{num1} / {num2} = {result}")
    elif chose == '5': 
        result = modulus(num1 , num2 )
        print(f"{num1} % {num2} = {result}")
    elif chose == '6': 
        result = gr(num1, num2)
        print(f"{num1} > {num2} = {result}")
    elif chose == '7': 
        result = ls(num1 , num2)
        print(f"{num1} < {num2} = {result}")
    elif chose == '8':
        result = gq(num1, num2)
        print(f"{num1} >= {num2} = {result}")
    elif chose == '9': 
        result = lq(num1, num2)
        print(f"{num1} <= {num2} = {result}")
    elif chose == '10 ':
        result = dq(num1, num2)
        print(f"{num1} == {num2} = {result}")
    elif chose == '11':
        result = fd(num1, num2)
        print(f"{num1} // {num2} = {result}")
    elif chose == '12': 
        result = expo(num1, num2)
        print(f"{num1} ** {num2} = {result}")
    else:
        print("Error: you have to write number or float type data because this is a calculator. ")

    