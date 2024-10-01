#Bank account 
class BankAccountL: 
    __balance = 0 
    def deposit(self, amount): 
        if amount >  0 : 
           self.__balance += amount 
           print("Deposit successfull")

        else:
            print("Invalid amount")
    def withdraw(self, amount): 
        if amount > 0  and amount <= self.__balance: 
          self.__balance -= amount 
          print("Withdraw successful")
        else: 
            print("Insufficent amount")
    def check_balance(self): 
        return self.__balance
ob = BankAccountL()
print(ob.check_balance())
print(ob.deposit(1000))
print(ob.check_balance())
print(ob.withdraw(600))
print(ob.check_balance())



#claculator 
def add(a , b):
    return a+ b 
def sub(a, b):
    return a - b 
def mul(a, b):
    return a * b 
def div(a, b): 
    return a / b 
def mod(a, b): 
    return a % b 
def calculator(): 
    print("Welcome to our calculator: ")

chose = input("Enter your chose(1.+/2.-/3.x/4.--/5.%)")
if chose in ['1', '2', '3', '4', '5']: 
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second numner: "))
if chose == '1': 
    result = add(num1, num2) 
    print(f'{num1} + {num2} = {result}')
elif chose == '2': 
    result = sub(num1, num2)
    print(f'{num1} - {num2}')
elif chose =='3': 
    result = mul(num1, num2)
    print(f'{num1} x {num2} = {result}')
elif chose == '4': 
    result = div(num1 , num2) 
    print(f"{num1} / {num2} = {result}")
elif chose == '5': 
    result = mod(num1, num2)
    print(f'{num1} % {num2} = {result}')