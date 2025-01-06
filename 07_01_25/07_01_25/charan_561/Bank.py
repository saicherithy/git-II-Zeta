class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient balance or invalid amount.")

class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied interest of {interest}. New balance is {self.balance}.")

class CurrentAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=500):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print(f"Exceeds overdraft limit of {self.overdraft_limit}. Withdrawal denied.")

# Example Usage:
savings_account = SavingsAccount("SA123", 1000)
savings_account.deposit(500)
savings_account.apply_interest()

current_account = CurrentAccount("CA123", 2000)
current_account.withdraw(2500)
