class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

    def check_balance(self):
        print(f"Balance for {self.account_holder}: {self.balance}")

    def transfer(self, amount, target_account):
        if amount > 0 and amount <= self.balance:
            self.withdraw(amount)
            target_account.deposit(amount)
            print(f"Transferred {amount} to {target_account.account_holder}.")
        else:
            print("Insufficient funds for transfer.")


# Example usage
account1 = BankAccount("Ashwini", 1000)
account2 = BankAccount("Harini", 500)

account1.deposit(200)          # Alice deposits 200
account1.withdraw(100)         # Alice withdraws 100
account1.check_balance()       # Check Alice's balance

account1.transfer(300, account2)  # Alice transfers 300 to Bob
account2.check_balance()       # Check Bob's balance
