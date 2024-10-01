#Access modifire type data 
class car : 
    brand = "Toyota"
def display(self):
    print(f"Our Brand Name is {self.brand }")
obj = car()
print(obj.brand)











#Encapsulation type data 
#Bank project 
class BankAccount: 
    __balance = 0 
    def deposit(self, amount): 
        if amount > 0 : 
            self.__balance += amount 
            print("Deposit successfull")
        else:
            print("Invalid amount")
    def withdraw(self, amount): 
        if amount > 0 and amount <= self.__balance : 
            self.__balance -=  amount 
            print("Withdraw successfull")
        else:
            print("Insufficiesnt amount")
    def check_balance(self): 
        return self.__balance
ob = BankAccount()
ob.deposit(100)
ob.withdraw(100)
print(ob.check_balance())
print(ob.deposit(1000))
