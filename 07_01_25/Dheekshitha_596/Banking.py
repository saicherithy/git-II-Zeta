# Transaction class to log transactions
class Transaction:
    def __init__(self, transaction_id, amount, type, date):
        self.transaction_id = transaction_id
        self.amount = amount
        self.type = type  # Deposit, Withdrawal, Transfer
        self.date = date

# Account superclass
class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []  # List to store transaction history

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            transaction = Transaction(len(self.transactions) + 1, amount, 'Deposit', '2025-01-06')
            self.transactions.append(transaction)
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            transaction = Transaction(len(self.transactions) + 1, amount, 'Withdrawal', '2025-01-06')
            self.transactions.append(transaction)
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, target_account):
        if self.withdraw(amount):
            target_account.deposit(amount)
            transaction = Transaction(len(self.transactions) + 1, amount, 'Transfer', '2025-01-06')
            self.transactions.append(transaction)
            return True
        return False

    def view_transactions(self):
        for transaction in self.transactions:
            print(f"Transaction ID: {transaction.transaction_id}, Type: {transaction.type}, Amount: {transaction.amount}, Date: {transaction.date}")

# Savings Account class
class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, min_balance=1000):
        super().__init__(account_number, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            return super().withdraw(amount)
        print("Insufficient funds to maintain minimum balance in Savings Account.")
        return False

# Current Account class
class CurrentAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=5000):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            return super().withdraw(amount)
        print("Insufficient funds in Current Account.")
        return False

# Bank class to manage multiple accounts
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_type, balance=0):
        if account_number in self.accounts:
            return "Account number already exists"
        
        if account_type.lower() == "savings":
            account = SavingsAccount(account_number, balance)
        elif account_type.lower() == "current":
            account = CurrentAccount(account_number, balance)
        else:
            return "Invalid account type"
        
        self.accounts[account_number] = account
        return account

    def view_summary(self):
        print("\nAccount Summary:")
        for account_number, account in self.accounts.items():
            print(f"Account Number: {account.account_number}, Balance: {account.get_balance()}")

    def display_transactions(self, account_number):
        if account_number in self.accounts:
            print(f"\nTransactions for Account {account_number}:")
            self.accounts[account_number].view_transactions()
        else:
            print("Account not found")

# Driver code to test the implementation
def main():
    bank = Bank()
    
    # Create accounts
    account1 = bank.create_account("12345", "savings", 2000)
    account2 = bank.create_account("67890", "current", 3000)
    
    if isinstance(account1, str):
        print(account1)
        return
    if isinstance(account2, str):
        print(account2)
        return
    
    # View account details
    bank.view_summary()
    
    # Deposit money
    print("\nDepositing 500 into account 12345:")
    account1.deposit(500)
    print(f"Account 12345 balance: {account1.get_balance()}")
    
    # Withdraw money
    print("\nWithdrawing 1000 from account 67890:")
    account2.withdraw(1000)
    print(f"Account 67890 balance: {account2.get_balance()}")
    
    # Transfer money between accounts
    print("\nTransferring 500 from account 12345 to account 67890:")
    account1.transfer(500, account2)
    print(f"Account 12345 balance: {account1.get_balance()}")
    print(f"Account 67890 balance: {account2.get_balance()}")
    
    # Display transactions for account 12345
    bank.display_transactions("12345")
    
    # Display transactions for account 67890
    bank.display_transactions("67890")

if __name__ == "__main__":
    main()
