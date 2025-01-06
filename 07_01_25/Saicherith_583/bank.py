class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def view_details(self):
        print(f"Account {self.account_number}: Balance {self.balance}")

class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, minimum_balance=500):
        super().__init__(account_number, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount >= self.minimum_balance:
            super().withdraw(amount)
        else:
            print("Cannot withdraw. Minimum balance required.")

class CurrentAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=1000):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Overdraft limit exceeded.")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_type, account_number, balance=0):
        if account_type == "savings":
            account = SavingsAccount(account_number, balance)
        else:
            account = CurrentAccount(account_number, balance)
        self.accounts[account_number] = account
        print(f"{account_type.capitalize()} Account {account_number} created.")

    def view_all_accounts(self):
        for account in self.accounts.values():
            account.view_details()

# Sample usage
bank = Bank()
bank.create_account("savings", "12345", 1000)
bank.create_account("current", "67890", 500)

bank.accounts["12345"].deposit(200)
bank.accounts["12345"].withdraw(800)
bank.accounts["67890"].withdraw(600)

bank.view_all_accounts()