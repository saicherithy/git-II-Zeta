class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder 
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: {self.balance}"

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.03):
        super().__init__(account_holder, balance) 
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied: {interest}. New balance: {self.balance}")

class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance=0, monthly_fee=10):
        super().__init__(account_holder, balance) 
        self.monthly_fee = monthly_fee

    def deduct_fee(self):
        self.balance -= self.monthly_fee
        print(f"Monthly fee of {self.monthly_fee} deducted. New balance: {self.balance}")

if __name__ == "__main__":
    
    account1 = BankAccount("Hello world", 500)
    account1.deposit(200)
    account1.withdraw(100)
    print(account1)

    # Create a savings account
    savings_account = SavingsAccount("Kavya", 1000, 0.05)
    savings_account.apply_interest()
    savings_account.deposit(500)
    print(savings_account)

    # Create a checking account
    checking_account = CheckingAccount("BBBB", 1500, 20)
    checking_account.deduct_fee()
    checking_account.withdraw(200)
    print(checking_account)
