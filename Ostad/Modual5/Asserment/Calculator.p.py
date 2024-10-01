def add(a,b):
    return a + b 

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b 

def div(a,b):
    return a / b

def ex(a,b):
    return a ** b

def fdiv(a,b):
    return a // b

def gr(a,b):
    return a > b 

def ls(a,b):
    return a < b

def gq(a,b):
    return a >= b

def lq(a,b):
    return a <= b 

def dq(a,b):
    return a == b 

def mo(a, b):
    return a % b 

def calculator():
    print("Selector operation")
   
chose = input("Enter your chose (1.add/2.sub/3.mul/4.div/5.ex/6.fdiv/7.gr/8.ls/9.gq/10.lq/11.dq/12.mo): ")
if chose in ('1','2','3','4','5','6', '7', '8','9','10','11', '12'):
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
if chose == "1":
        result = (num1,num2)
        print(f"{num1} + {num2} = {result}")

elif chose == "2":
    result = add(num1, num2)
    print(f"{num1} - {num2} = {result}")

elif chose == "3":
    result = sub(num1, num2)
    print(f"{num1} * {num2} = {result}")

elif chose == "4": 
    result = mul(num1, num2)
    print(f"{num1} / {num2} = {result}")

elif chose == "5":
    result = div(num1,num2)
    print(f"{num1} ** {num2} = {result}")

elif chose == "6":
    result = ex(num1, num2)
    print(f"{num1} // {num2} = {result}")

elif chose == "7": 
    result = fdiv(num1, num2)
    print(f"{num1} > {num2} = {result}")

elif chose == "8": 
    result = (num1, num2)
    print(f"{num1} < {num2} = {result}")

elif chose == "9": 
    result = (num1, num2)
    print(f"{num1} >= {num2} = {result}")

elif chose == "10":
    result = (num1, num2)
    print(f"{num1} <= {num2} = {result}")

elif chose == "11":
    result = (num1, num2)
    print(f"{num1} == {num2} = {result}")

elif chose == "12": 
    result = (num1, num2)
    print(f"{num1} % {num2} = {result}")

else:
    print("Error")


calculator()
















