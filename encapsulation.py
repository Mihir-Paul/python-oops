#Encapsulation

#Bad Programming
class BadBankAccount():
    def __init__(self,balance):
        self.balance = balance

account = BadBankAccount(0.0)
account.balance = -1
print(account.balance)

#Programming with encapsulation

class BankAccount():
    def __init__(self,balance):
        self._balance = balance 

    @property
    def balance(self):
        return self._balance

    def deposit(self,amount):
        new_amount = amount
        if self._is_valid_amount(new_amount):
            raise ValueError("Amount must be positive")
        self._balance += new_amount 

    def withdraw(self,amount):
        new_amount = amount 
        if self._is_valid_amount(new_amount):
            raise ValueError("Amount must be positive")
        elif new_amount>self._balance:
            raise ValueError("Insufficient Balance")
        self._balance -= new_amount
    


    def _is_valid_amount(self,amount):
        return amount<0 
    
account = BankAccount(900)
account.deposit(900)
print(account.balance)
account.withdraw(200)
print(account.balance)