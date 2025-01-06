class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, account):
        self.accounts.append(account)
        print(f"Account {account.account_number} created successfully!")

    def view_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                account.display_account_details()
                return
        print("Account not found.")

    def view_all_accounts(self):
        for account in self.accounts:
            account.display_account_details()

    def transfer_funds(self, from_acc_no, to_acc_no, amount):
        from_account = None
        to_account = None

        for account in self.accounts:
            if account.account_number == from_acc_no:
                from_account = account
            if account.account_number == to_acc_no:
                to_account = account

        if not from_account or not to_account:
            print("Invalid account details.")
            return

        if from_account.withdraw(amount):
            to_account.deposit(amount)
            print(f"Transferred {amount} from {from_acc_no} to {to_acc_no}.")

    def display_transaction_history(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                account.display_transactions()
                return
        print("Account not found.")


class Account:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        self.balance += amount
        self.add_transaction(f"Deposited: {amount}")
        return True

    def withdraw(self, amount):
        raise NotImplementedError("This method should be overridden in subclasses.")

    def view_balance(self):
        print(f"Account {self.account_number}: Balance = {self.balance}")

    def add_transaction(self, description):
        self.transactions.append(description)

    def display_account_details(self):
        print(f"Account Number: {self.account_number}, Holder: {self.holder_name}, Balance: {self.balance}")

    def display_transactions(self):
        print(f"Transaction history for account {self.account_number}:")
        for transaction in self.transactions:
            print(transaction)


class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, balance, minimum_balance):
        super().__init__(account_number, holder_name, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print("Cannot withdraw: Minimum balance requirement not met.")
            return False
        self.balance -= amount
        self.add_transaction(f"Withdrew: {amount}")
        return True


class CurrentAccount(Account):
    def __init__(self, account_number, holder_name, balance, overdraft_limit):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance - amount < -self.overdraft_limit:
            print("Cannot withdraw: Overdraft limit exceeded.")
            return False
        self.balance -= amount
        self.add_transaction(f"Withdrew: {amount}")
        return True


# Example usage
bank = Bank()
savings = SavingsAccount("1001", "Alice", 5000, 1000)
current = CurrentAccount("1002", "Bob", 2000, 500)

bank.create_account(savings)
bank.create_account(current)

bank.view_all_accounts()

savings.deposit(1500)
current.withdraw(1000)
current.withdraw(3000)  # Should fail due to overdraft

bank.transfer_funds("1001", "1002", 2000)

bank.display_transaction_history("1001")
bank.display_transaction_history("1002")
