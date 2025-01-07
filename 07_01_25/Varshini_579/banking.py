class Account:
    account_counter = 1000  # Class variable for unique account numbers

    def __init__(self, name, initial_balance):
        self.account_number = Account.account_counter
        Account.account_counter += 1
        self.name = name
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transactions.append(f"Deposited: ${amount}")
        print(f"${amount} deposited successfully.")

    def withdraw(self, amount):
        raise NotImplementedError("Withdraw method must be implemented by subclasses.")

    def view_balance(self):
        return f"Account Number: {self.account_number}, Balance: ${self.balance}"

    def view_transaction_history(self):
        return self.transactions if self.transactions else ["No transactions yet."]


class SavingsAccount(Account):
    def __init__(self, name, initial_balance, minimum_balance=500):
        super().__init__(name, initial_balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance - amount < self.minimum_balance:
            raise ValueError("Cannot withdraw. Minimum balance requirement not met.")
        self.balance -= amount
        self.transactions.append(f"Withdrew: ${amount}")
        print(f"${amount} withdrawn successfully.")


class CurrentAccount(Account):
    def __init__(self, name, initial_balance, overdraft_limit=1000):
        super().__init__(name, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance - amount < -self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded.")
        self.balance -= amount
        self.transactions.append(f"Withdrew: ${amount}")
        print(f"${amount} withdrawn successfully.")


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_type, name, initial_balance):
        if account_type == "Savings":
            account = SavingsAccount(name, initial_balance)
        elif account_type == "Current":
            account = CurrentAccount(name, initial_balance)
        else:
            raise ValueError("Invalid account type.")
        self.accounts.append(account)
        print(f"Account created successfully. Account Number: {account.account_number}")
        return account

    def view_all_accounts(self):
        return [account.view_balance() for account in self.accounts]

    def view_account_details(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account.view_balance()
        raise ValueError("Account not found.")

    def transfer_funds(self, from_account_number, to_account_number, amount):
        from_account = next((acc for acc in self.accounts if acc.account_number == from_account_number), None)
        to_account = next((acc for acc in self.accounts if acc.account_number == to_account_number), None)
        if not from_account or not to_account:
            raise ValueError("One or both account numbers are invalid.")
        from_account.withdraw(amount)
        to_account.deposit(amount)
        print(f"${amount} transferred successfully from {from_account_number} to {to_account_number}.")
