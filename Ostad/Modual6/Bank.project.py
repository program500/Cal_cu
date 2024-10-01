class Bankaccount: 
    __balance = 0 

    def deposit(self,ammount): 
        if ammount > 0 : 
         self.__balance += ammount
          print("Deposit success")
        else: 
            print("Invalid account")
def withdaraw(self,ammount):
    if ammount >0 and ammount <= self.__balance: 
        self.__balance -= ammount
        print("Withdraw")
    else: 
        print("Insufficent ammount")
def check_balance(self):
        n = 20
obj = Bankaccount()



