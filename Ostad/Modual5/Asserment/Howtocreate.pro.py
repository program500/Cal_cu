def add(a, b):
    return a + b 
def sub(a, b):
    return a - b 
def mul(a, b):
    return a * b
def div(a, b ):
    return a / b 
def ex(a, b):
    return a ** b 
def fdiv(a,b): 
    return a // b 
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
def mod(a, b):
    
    return a % b 
def calculator():
    print("1.add")
    print("2.sub")
    print("3.mul")
    print("4.div")
    print("5.ex")
    print("6.fdiv")
    print("7.gr")
    print("8.ls")
    print("9.gq")
    print("10.lq")
    print("11.dq")
    print("12.mod")
chose = input("Enter your chose:(1.addition/2.subtraction/3.multiplication/4.diviaion/5.exponendiation/6.floordivision/7.greaterthan/8.lessthan/9.greaterequal/10.lessthenequal/11.dobulaequal/12.modulus)")
if chose in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:

  num1 =float(input("Enter your first number: "))

  num2 =float(input("Enter your second number: "))
if chose == '1':
    result = (num1, num2)
    print(f"{num1} + {num2} = {result}")
elif chose == '2':
    result = (num1, num2)
    print(f"{num1} - {num2} = {result}")
elif chose == '3':
    result = (num1, num2)
    print(f"{num1} * {num2} = {result} ")
elif chose == '4': 
    result = (num1, num2)
    print(f"{num1} / {num2} = {result}")
elif chose == '5': 
    result = (num1, num2)
    print(f"{num1} ** {num2} = {result}")
elif chose == '6': 
    result = (num1, num2)
    print(f"{num1} // {num2} = {result}")
elif chose == '7': 
    result = (num1, num2)
    print(f"{num1} > {num2} = {result}")
elif chose == '8':
    result = (num1, num2)
    print(f"{num1} < {num2} = {result}")
elif chose == '9': 
    result = (num1, num2)
    print(f"{num1} >= {num2} = {result}")
elif chose == '10':
    result = (num1, num2)
    print(f"{num1} <= {num2} = {result} ")
elif chose == '11': 
    result = (num1, num2)
    print(f"{num1} == {num2} = {result}")
elif chose == '12': 
     result = (num1, num2)
     print(f"{num1} % {num2} = {result}")
