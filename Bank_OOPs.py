import time
from datetime import datetime
class bank_account:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
        pass
    def display_balance(self):
        time.sleep(0.8)
        latest = datetime.now()
        print("Date:",latest.date())
        print("Time:",latest.time())
        print("Balance remaining : ",self.balance)
        print("\n","\n")
        pass
    def deposit_amount(self):
        time.sleep(0.5)
        amount = int(input("Enter the amount to deposit :"))
        time.sleep(0.5)
        self.balance += amount
        latest = datetime.now()
        print("Date:",latest.date())
        print("Time:",latest.time())
        print("Deposited Amount : ",amount)
        time.sleep(0.8)
        print("New Balance : ",self.balance)
        print("\n","\n")
        pass
    def withdraw(self):
        time.sleep(0.5)
        withamount= int(input("Enter the amount to withdraw :"))
        time.sleep(0.3)
        if withamount<=self.balance:
            self.balance-=withamount
            latest = datetime.now()
            print("Date:",latest.date())
            print("Time:",latest.time())
            print("Withdrawed Amount :",withamount)
            time.sleep(0.5)
            print("New Balance : ",self.balance)
            print("\n","\n")
        else:
            print("Insuffient Funds")
            print("\n","\n")
        pass
acc1 = bank_account("Harish Udhayakumar Sumathi",30000)
acc1.display_balance()
acc1.deposit_amount()
acc1.withdraw()
