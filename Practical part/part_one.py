class BankAccount:
    interest_rate = 0.05

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount 


    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def apply_interest(self):
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest

    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: {self.balance}")


# Create two instances of BankAccount
account1 = BankAccount("John Doe")
account2 = BankAccount("Jane Smith")

# Perform deposits and withdrawals
account1.deposit(1000)
account1.withdraw(500)
account2.deposit(2000)
account2.withdraw(100)

# Apply interest
account1.apply_interest()
account2.apply_interest()

# Display account information
account1.display_account_info()
account2.display_account_info()