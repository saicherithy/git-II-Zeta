class Account:
    """Superclass for common account attributes and methods."""
    def _init_(self, account_number, account_holder, balance):
        self._account_number = account_number
        self._account_holder = account_holder
        self._balance = balance
        self._transaction_history = []

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive."
        self._balance += amount
        self._transaction_history.append(f"Deposited: {amount}")
        return "Deposit successful."

    def withdraw(self, amount: float):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > self._balance:
            return "Insufficient balance."
        self._balance -= amount
        self._transaction_history.append(f"Withdrew: {amount}")
        return "Withdrawal successful."

    def transfer(self, amount: float, target_account):
        if amount <= 0:
            return "Transfer amount must be positive."
        withdrawal_message = self.withdraw(amount)
        if "successful" not in withdrawal_message:
            return withdrawal_message
        target_account.deposit(amount)
        self._transaction_history.append(f"Transferred: {amount} to Account {target_account._account_number}")
        return "Transfer successful."

    def view_details(self):
        return f"Account Number: {self._account_number}\nAccount Holder: {self._account_holder}\nBalance: {self._balance}"

    def get_transaction_history(self):
        return "\n".join([f"- {transaction}" for transaction in self._transaction_history])


class SavingsAccount(Account):
    """Savings account with a minimum balance requirement."""
    def _init_(self, account_number: int, account_holder: str, balance: float = 0.0, min_balance: float = 100.0):
        super()._init_(account_number, account_holder, balance)
        self.min_balance = min_balance

    def withdraw(self, amount: float):
        if self._balance - amount < self.min_balance:
            return "Cannot withdraw: Minimum balance requirement not met."
        self._balance -= amount
        self._transaction_history.append(f"Withdrew: {amount}")
        return "Withdrawal successful."


class Bank:
    """Bank entity to manage accounts and transactions."""
    def _init_(self):
        self.accounts = {}
        self.next_account_number = 1

    def create_account(self, account_holder: str, account_type: str, initial_balance: float = 0.0):
        account_number = self.next_account_number
        self.next_account_number += 1

        if account_type == "Savings":
            account = SavingsAccount(account_number, account_holder, initial_balance)
        else:
            return "Invalid account type. Choose 'Savings'."

        self.accounts[account_number] = account
        return account_number

    def view_all_accounts(self):
        for account in self.accounts.values():
            print(account.view_details())

    def get_transaction_history(self, account_number: int):
        if account_number not in self.accounts:
            return "Invalid account number."
        print(f"Transaction History for Account {account_number} ({self.accounts[account_number]._account_holder}):")
        print(self.accounts[account_number].get_transaction_history())


# Example Usage
if _name_ == "_main_":
    bank = Bank()

    # Create Arjun's account
    bank.create_account("Arjun", "Savings", 500.0)

    # Perform Transactions
    arjun_account = bank.accounts[1]  # Access Arjun's account directly via account number

    print(arjun_account.deposit(100.0))  # Output: Deposit successful.
    print(arjun_account.withdraw(50.0))  # Output: Withdrawal successful.
    print(arjun_account.transfer(200.0, arjun_account))  # Transfer to the same account (Arjun to Arjun)

    # View Arjun's account details and transaction history
    print("\nView Account Details for Arjun:")
    bank.view_all_accounts()

    print("\nView Transaction History for Arjun:")
    bank.get_transaction_history(1)

    # Show current balance after transactions
    print(f"\nCurrent Balance for Arjun: {arjun_account._balance}")