#A static method is a method that belongs to the class itself and not any instance 

# we use the decorator @staticmethod to define a static method 

class BankAccount():
    Min_Balance = 100

    def __init__(self,owner,balance):
        self.owner = owner 
        self._balance = balance 

    def deposit(self,amount):
        new_amount = amount 
        if self._is_valid_amount(new_amount):
            self._balance+= new_amount 
            self.__log_transaction("Deposit",new_amount)
        else:
            print("Amount must be positive")

    def _is_valid_amount(self,amount):
        return amount>0

    def __log_transaction(self,transaction_type,amount):
        print(f"Logging {transaction_type} of {amount}.\nBalance: {self._balance} ")

    @staticmethod
    def interest(rate):
        return 0<rate<10
    
account = BankAccount("Mihir",200)
account.deposit(500)
print(BankAccount.interest(90))