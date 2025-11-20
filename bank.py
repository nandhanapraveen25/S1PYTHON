class BankAccount:
    def __init__(self, account_number, name, account_type, balance):
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("New balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("New balance:", self.balance)
        else:
            print("Insufficient balance!")
account_number = input("Account number: ")
name = input("Name: ")
account_type = input("Account type: ")
balance = float(input("Initial balance: "))
acc = BankAccount(account_number, name, account_type, balance)
acc.deposit(float(input("Deposit amount: ")))
acc.withdraw(float(input("Withdraw amount: ")))
print("Final balance:", acc.balance)
