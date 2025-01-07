class Account:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif self.__balance < amount:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
    
    def get_balance(self):
        return self.__balance
    
    def get_details(self):
        return f"Account Number: {self.__account_number}, Balance: {self.__balance}"

class SavingsAccount(Account):
    def __init__(self, account_number, balance, min_balance):
        super().__init__(account_number, balance)
        self.__min_balance = min_balance

    def withdraw(self, amount):
        if self.get_balance() - amount < self.__min_balance:
            print(f"Withdrawal denied. Minimum balance of {self.__min_balance} must be maintained.")
        else:
            super().withdraw(amount)

    def get_details(self):
        return super().get_details() + f", Minimum Balance: {self.__min_balance}"

class CurrentAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.__overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.get_balance() + self.__overdraft_limit < amount:
            print(f"Withdrawal denied. Overdraft limit of {self.__overdraft_limit} exceeded.")
        else:
            super().withdraw(amount)

    def get_details(self):
        return super().get_details() + f", Overdraft Limit: {self.__overdraft_limit}"

class Bank:
    def __init__(self):
        self.__accounts = {}

    def create_account(self, account_type, account_number, balance, min_balance=None, overdraft_limit=None):
        if account_number in self.__accounts:
            print("Account number already exists.")
            return
        
        if account_type == 'savings':
            if min_balance is None:
                print("Minimum balance is required for Savings Account.")
            else:
                account = SavingsAccount(account_number, balance, min_balance)
                self.__accounts[account_number] = account
        elif account_type == 'current':
            if overdraft_limit is None:
                print("Overdraft limit is required for Current Account.")
            else:
                account = CurrentAccount(account_number, balance, overdraft_limit)
                self.__accounts[account_number] = account
        else:
            print("Invalid account type.")
    
    def view_all_accounts(self):
        if not self.__accounts:
            print("No accounts to display.")
        else:
            for account in self.__accounts.values():
                print(account.get_details())
    
    def get_account(self, account_number):
        if account_number in self.__accounts:
            return self.__accounts[account_number]
        else:
            print("Account not found.")
            return None


bank = Bank()


bank.create_account('savings', '123', 1000, 500)
bank.create_account('current', '456', 2000, overdraft_limit=1000)


account_123 = bank.get_account('123')
if account_123:
    account_123.deposit(500)


account_456 = bank.get_account('456')
if account_456:
    account_456.withdraw(2500) 


bank.view_all_accounts()


if account_123:
    account_123.withdraw(600)
