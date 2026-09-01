import random 
class BankAccount:
    def __init__(self,name,number, balance):
        self.name = name
        self.number = number
        self.__balance = balance
        

    @property
    def balance(self):
        return self.__balance
        
    @balance.setter
    def balance(self,balance):
        self.__balance = balance

    def deposit(self,amount):
        if amount <= 0:
            print("Seriously ?")
            return False
        else:
            self.balance += amount
            return True

    def withdraw(self,amount):
        if self.balance < amount:
            print("You don't have enough balance in account")
            return False
        else:
            self.balance -= amount
            return True

    def __str__(self):
        return f"Name: {self.name}, Account number: {self.number} , Balance: {self.balance}"

    def __eq__(self,other):
        return self.number == other.number


class SavingAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance - amount < 1000:
            print("You can't withdraw",amount)
            return False
        else:
            self.balance -= amount
            return True

class Bank:
    def __init__(self):
        self.accounts = []

    def addAccount(self,obj):
        self.accounts.append(obj)

    def displayAccounts(self):
        for acc in self.accounts:
            print(acc)

    def __str__(self):
        return( f"Name:{self.name} Number: {self.number}, Balance: {self.balance}")
        
    def displayAccount(self,number):
        for acc in self.accounts:
            if acc.number == number:
                print(f"Name: {acc.name} Balance: {acc.balance}")
                break

        else:
            print("Account doesn't exist")

    def getAccount(self):
        number = int(input("Enter number: "))
        for acc in self.accounts:
            if acc.number == number:
                return acc
        else:
            print("Account not found")


bank = Bank()
while True:
    choice = int(input("Choose an option\n1.Add account\n2.Deposit\n3.Withdraw\n4.Show account\n5.Show all accounts\n6.Exit\n"))

    match choice:
        case 1:
            name = input("Enter name: ")
            balance = int(input("Enter balance: "))
            number = random.randint(100000,999999)
            account_type = int(input("Do you want current account or saving account?\npress 1 for normal account. 2 for saving account"))
            if account_type == 1:
                acc = BankAccount(name, number,balance)
            elif account_type == 2:
                acc = SavingAccount(name, number,balance)
            else:
                print("Invalid input")

            bank.addAccount(acc)
            print("Account created\nYour numbers is ",number)

        case 2:
         while True:
            acc = bank.getAccount()
            amount = int(input("Enter amount: "))
            if acc.deposit(amount):
                print("Amount deposited successfully")
                break

        case 3:
         while True:
            acc = bank.getAccount()
            amount = int(input("Enter amount: "))
            if acc.withdraw(amount):
                print("Amount withdrawn successfully")
                break

        case 4:
         number = int(input("Enter number: "))
         bank.displayAccount( number)

        case 5:
            bank.displayAccounts()

        case 6:
            break
        case _:
            print("Invalid input")











    

    