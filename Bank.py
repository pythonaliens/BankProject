import sys
class Customer:

    def __init__(self,username,accountnumber,password):
        self.username = username
        self.accountnumber = accountnumber
        self.password = password
    def signup(self):
            print("Account successfully created",self.username)
            print("Your Username is : ", self.username)
            print("Your Accountnumber is : ", self.accountnumber)
            print("Your password is : ",self.password)


class Account:

    def __init__(self,balance=0,minamount=500,):
        self.balance = balance
        self.minamount = minamount
        self.firsttime = True

    def deposit(self,amount):
        if amount>0:

            if amount>=self.minamount or self.balance>=self.minamount:
                    print(amount)
                    self.balance=amount+self.balance
                    print("sucessfully deposited amount : ",self.balance)
            else:
                print("Please Deposit Minimum Amount")

        else:
            print("Negative amount not allowed")

    def withDraw(self,amount):
        if amount>0:
                tempbalance = self.minamount
                tempbalance=self.balance - amount
                if(tempbalance>=500):
                    self.balance = self.balance - amount
                else:
                    print("Ensufficient Funds to remove", amount)

        else:
            print("Negitive Amount Not Allowed")

    def checkBalance(self):
        print("current balance is :",self.balance)

    def exit(self):
        sys.exit()
bankdetails = Account()
account = Account()
class MainProgram:

    while True:
        print(" 1-SignUp\n 2-SignIn")
        option = int(input("Choose your option"))
        if option == 1:
            username = input("Enter the username")
            accountnumber = input("Please enter account number")
            password = input("Please choose any password")
            amount = int(input("Enter the initial amount"))
            account.deposit(amount)
            if amount>=500:
                customerclass = Customer(username, accountnumber, password)
                customerclass.signup()
            else:
                print("account creation failed sign up again")

        if option == 2:
            loop = True
            while loop:
                print("1-Enter your password\n 2: Exit")
                option = int(input("Enter your option"))
                if option ==1:
                    password = input("Please Enter your password")
                    if password =="acc":
                        while True:
                            print(" 1-Deposit\n 2-Withdraw\n 3-CheckBalance\n 4-Logout")
                            option = int(input("Choose any one of the options"))
                            if option == 1:
                                amount = int(input("Enter the amount to Deposit"))
                                account2.deposit(amount)
                            if option == 2:
                                amount = int(input("Enter the amount to Withdraw"))
                                account.withDraw(amount)
                            if option == 3:
                                account.checkBalance()
                            if option == 4:
                                break
                    loop = False











