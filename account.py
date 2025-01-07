class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number 
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return self.balance

class SavingsAccount(Account):
    def __init__(self, account_number, name, balance):
        super().__init__(account_number, name, balance)
        self.limit = 40000  
    
    def withdraw(self, amount):
        if amount > self.limit:
            return "Cannot withdraw beyond the limit"
        if amount > self.balance:
            return "Insufficient balance"
        return super().withdraw(amount)

class CurrentAccount(Account):
    def __init__(self, account_number, name, balance):
        super().__init__(account_number, name, balance)
        self.od_limit = 10000  

    def withdraw(self, amount):
        if amount > self.balance + self.od_limit:  
            return "Cannot withdraw beyond the overdraft limit"
        return super().withdraw(amount)
                  
# Creating a generic Account object
account = Account(account_number=101, name="John Doe", balance=5000)
print("Initial Account Balance:", account.balance)
print("After Deposit:", account.deposit(2000))
print("After Withdrawal:", account.withdraw(3000))
print("Attempt Withdrawal Exceeding Balance:", account.withdraw(5000))
print()

# Creating a SavingsAccount object
savings_account = SavingsAccount(account_number=102, name="Jane Doe", balance=10000)
print("Initial Savings Account Balance:", savings_account.balance)
print("After Deposit:", savings_account.deposit(5000))
print("After Withdrawal Within Limit:", savings_account.withdraw(20000))
print("Attempt Withdrawal Beyond Limit:", savings_account.withdraw(50000))
print()

# Creating a CurrentAccount object
current_account = CurrentAccount(account_number=103, name="Alice", balance=15000)
print("Initial Current Account Balance:", current_account.balance)
print("After Deposit:", current_account.deposit(5000))
print("After Withdrawal Within Overdraft Limit:", current_account.withdraw(25000)) 
print("Attempt Withdrawal Beyond Overdraft Limit:", current_account.withdraw(35000))
