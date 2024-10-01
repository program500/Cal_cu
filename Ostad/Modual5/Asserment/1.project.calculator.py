def add(x, y):
                  # Firstable, i have to add two numbers in function 
    return x + y

def substrc(x, y): 
                    # Secondly, i have to substraction two numbers in function and return 
    return x - y 

def multiplication(x, y):

    return x * y      #Thirdly, I have to multiplication two numbers in function

def division(x, y):

    return x / y  # Forthly , I have to division two numbers in function 

def modulus(x, y): 
                   # Then , I have to modulus two numbers in functon 
    return x % y  

def exponentiation(x, y):
                              # After that, i have to exponentiation two numbers in function 
    return x ** y 

def floordivision(x, y):
    return x // y             #and Eventually i have  to floordivision two numbers in function 

def gr(x,y):

    return x > y 

def ls(x,y):

    return x < y 
def gq(x,y):

    return x >= y 

def lq(x,y):

    return x <= y

def dq(x,y):

    return x == y

def calculator():
    print("Select operation ")
    print("1.add")
    print("2.substrc")
    print("3.multiplication")
    print("4.division")
    print("5.modulus")
    print("6.exponentiation")
    print("7.floordivision")
    print("8.gr")
    print("9.ls")
    print("10.gq")
    print("11.lq")
    print("12.dq")
chose = input("Enter your chose(1/2/4/5/6/7/8/9/10/11/12): ")
if chose in ['1','2','3','4','5','6','7','8','9','10','11','12']:
    
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
if chose == '1':
    result = add(num1, num2)
    print(f"{num1} + {num2} = {result}")
elif chose == '2':
    result = substrc(num1, num2)
    print(f"{num1} - {num2} = {result}")
elif chose == '3':
    result  = multiplication(num1, num2)
    print(f"{num1} * {num2} = {result}")
elif chose == '4':
    result = division(num1, num2) 
    print(f"{num1} / {num2} = {result}")
elif chose == "5":
     result = modulus(num1, num2)
     print(f"{num1} % {num2} = {result}")
elif chose == '6':
     result = exponentiation(num1, num2)
     print(f"{num1} ** {num2} = {result}")
elif chose == '7':
     result = floordivision(num1, num2)
     print(f"{num1} // {num2} = {result}")
elif chose == '8':
    result = gr(num1, num2)
    print(f"{num1} > {num2} = {result}")
elif chose == '9':
    result = ls(num1, num2)
    print(f"{num1} < {num2} = {result}")
elif chose == '10':
    result = gq(num1, num2)
    print(f"{num1} >= {num2} = {result}")
elif chose == '11':
    result = lq(num1, num2 )
    print(f"{num1} <= {num2} = {result}")
elif chose == '12':
    result = dq(num1, num2)
    print(f"{num1} == {num2} = {result}")



         