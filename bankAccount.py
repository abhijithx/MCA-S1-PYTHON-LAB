class BankAccount:
    
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
        print("BankAccount constructor called.")

    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New Balance: ₹{self.balance}")

    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}. Remaining Balance: ₹{self.balance}")

    
    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.holder_name}")
        print(f"Balance: ₹{self.balance}")

acc1 = BankAccount("BA1001", "Alice", 5000)


acc1.display()
acc1.deposit(2000)
acc1.withdraw(1000)
acc1.display()
