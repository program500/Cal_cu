#Claculator 
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
def fd(a, b) :
    return a // b 

def gr(a, b): 
    return a > b 
def ls(a, b) : 
    return a < b 
def gq(a, b) :
    return a >= b 
def lsq(a, b) :
    return a <= b 
def dq(a, b) : 
    return a == b
def modu(a, b): 
    return a % b 
chose = input("1.addition/2.subtruction/3.multiplication/4.division/5.exponentiation/6.floordivision/7.greaterthan/8.lessthan/9.greatterthanequla/10.lessthanequal/11.Dobuleequla/12.Modulus")

if chose in('1','2', '3','4', '5','6', '7', '8', '9', '10','11','12'): 
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
if chose == '1': 
    result = add(num1, num2)
    