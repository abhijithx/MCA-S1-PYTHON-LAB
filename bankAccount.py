class BankAccount:

  def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
 
  def display_balance(self):
    print(f"Account owner: {self.owner}")
    print(f"Current balance: {self.balance}")       


    

  def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

  def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. Remaining balance is {self.balance}.")

    


account =BankAccount("Abhijith", 1000)
account.display_balance()
account.deposit(500)
account.withdraw(200)
account.display_balance()
