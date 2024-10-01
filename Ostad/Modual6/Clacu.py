#Python banking programm
def Show_balance():
    print(f"your balance is $ {balance}.2f")
def Deposit():
    ammount = float(input("Enter your an ammount to be deposited: "))
    if ammount < 0 : 
        print("That is not valid ammount.")
        return 0 
    else: 
        return ammount
def withdraw():
    amount = float(input("Enter your ammount withdraw ammount: "))
    if amount > balance: 
        print("Insufficient funds")
        return 0 
    elif amount < 0: 
        print("Ammount must be greater than 0")
        return 0 
    else: 
        return amount
def main():
    balance = 0 
    is_running = True


while is_running: 
    print("Banking programm")
    print("1.Show_balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    chose = input("Enter your chose(1,2,3,4)")
    if chose == "1": 
      Show_balance()
    elif chose == "2": 
        balance += Deposit
    elif chose == "3": 
        balance -= withdraw
    elif chose == "4": 
        is_running = False

    else: 
        print("Invalid balance ")
 
print("Thank you! Have a nice day.")