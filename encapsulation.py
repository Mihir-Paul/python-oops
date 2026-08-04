#Encapsulation

#Bad Programming
class BadBankAccount():
    def __init__(self,balance):
        self._balance = balance
        
account = BadBankAccount(0.0)
account._balance = -1
print(account._balance)

#Programming with encapsulation
class BankAccount():
    def __init__(self,balance):
        self._balance = balance 
        
    @property
    def balance(self):
        return self._balance
    
    def deposit(self,amount):
        if amount<=0:
            raise ValueError("Deposit amount must be positive")
        self._balance+= amount
        
    def withdraw(self,amount):
        if amount<=0:
            raise ValueError("Withdraw amount must be positive")
        elif amount>=self._balance:
            raise ValueError("Balance amount is less")
        self._balance -= amount 
        
account = BankAccount(900)
account.deposit(200)
print(account.balance)
account.withdraw(800)
print(account.balance)