#project 02 in the remote job
class Hasip: 
    x = 10 
    y =  20 
    sum = x + y 
s = Hasip()
print(Hasip.sum)
#Bangking project 02 

class Bank: 

    def __init__(self, Holder_name, initial_dipposit_balance):
        self.Holder_name= Holder_name
        self.blance = initial_dipposit_balance

#Ostad = Bank('Xyz', 1000)

def deposite(self, ammount):
   self.blance += ammount

def get_blance(self):
    return self.blance

def withdraw(self, amount):
    if amount < self.blance:
        self.blance -= amount 
        return amount
    else:
        return f"insufficient blance"
ostad = Bank("xyz", 1000)
print(ostad.blance)

#print(Ostad.Holder_name)
#print(Ostad.blance)

