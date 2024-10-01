"""#caculator project 
def add(a, b): 
    return a + b 
def sub(a, b): 
    return a - b 
def mul(a,b): 
    return a * b 
def div(a, b) : 
    return a / b 
def select_option(): 
    a = 0 
chose = input("Enter your chose(1.addition/2.subtraction/3.multiplicatio/4.exponentiation): ")
if chose in ['1', '2', '3', '4'] : 
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))

if chose == '1': 
    result = add(num1, num2) 
    print(f"{num1} + {num2} = {result}")
elif chose == '2': 
    result = sub(num1, num2)  
    print(f"{num1} - {num2} = {result}") 
elif chose == '3': 
    result = mul(num1, num2) 
    print(f"{num1} x {num2} = {result}")
elif chose == '4': 
    result = div(num1, num2) 
    print(f"{num1} / {num2} = {result} ")
"""
class BankAccount: 
    __blance = 0 
    def deposit(self, amount) : 
        if amount >0  : 
            self.__blance += amount
            print("Deposit Successfull") 
        else: 
            print("Invalid amount")
    def withdraw(self, amount): 
        if amount > 0 and amount <= self.__blance: 
            self.__blance -= amount
            print("Withdraw successfull")
        else: 
            print("INsufficent amount") 
    def check_balance(self): 
        return self.__blance 
my_bankAccount = BankAccount() 
print(my_bankAccount.check_balance())
print(my_bankAccount.deposit(1000)) 
print(my_bankAccount.check_balance())