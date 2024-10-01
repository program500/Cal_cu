class BankAccount: 
    __balance = 0 
    def deposit(self, amount): 
        if amount > 0 : 
         self.__balance += amount 
         print("Deposit successfull")
    def withdraw(self, amount): 
        if amount > 0 and  amount <= self.__balance: 
           self.__balance -= amount 
           print("Withdraw successfull")
    def check_Balance(self): 
       return self.__balance
ob = BankAccount()
ob.deposit(1000)
ob.check_Balance()
print(ob.check_Balance())
print(ob.withdraw(550))
print(ob.check_Balance())