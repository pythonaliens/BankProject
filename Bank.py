import sys


class Customer:


    def __init__(self, name, balance=0,Ubalance=0):
        self.name = name
        self.balance = balance
        self.Ubalance = Ubalance

    def deposit(self, amt):
        if amt <= 500:
            print("Deposit the Minimum Amount >= 500")
        else:
            self.balance = self.balance + amt
            self.Ubalance = self.balance - 500
            print("Mininum balance to be maintained = 500")
            print("Current balance is ", self.Ubalance)

    def withdraw(self, amt):
        if amt > self.Ubalance:
            print("Insufficient funds")
            print("First deposit some amount")

        else:
            usable_balance = self.Ubalance - amt
            print("Mininum balance maintaining 500")
            print("After withdraw balance is ", usable_balance)


bankname = 'Durgasoft'
print("welcome to "+ bankname +" bank")
name = input("Enter your name :: ")
c = Customer(name)

while True:
    print(" d-Deposit\n w-Withdraw\n e-Exit")
    option = input("choose your option")
    if option.lower() == 'd':
        amt = float(input("Enter the amount to deposit"))
        c.deposit(amt)
    elif option.lower() == 'w':
        amt = float(input("Enter the amount to withdraw"))
        c.withdraw(amt)

    elif option.lower() == 'e':
        print("Thanks for banking")
        break
    else:
        print("choose valid option")
