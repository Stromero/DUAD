# Cree una clase de BankAccount que:
# a.tenga un atributo de balance.
# b.tenga un metodo para ingresar dinero.
# c.tenga un metodo para retirar dinero.

class BankAccount:

    balance = 0

    def __init__(self):
        pass
        

    def add_money_to_account(self, amount_parameter):
        self.balance += amount_parameter
        print(f'Balance on account is: ${self.balance}')
    
    def withdraw_money_from_account(self, amount_parameter):
        self.balance -= amount_parameter
        print(f'the amount you have susbtracted has been: ${amount_parameter} and the balance in the account is: ${self.balance}')
        

# Cree otra clase que herede de esta llamada SavingAccount que:
# a. Tenga un atributo de min_balance que se pueda asignar al crearla.
# b. Arroje un error si se intenta retirar dinero y el balance esta debajo del min_balance

class SavingAccount(BankAccount):

    minimun_balance = int

    def __init__(self, minimun_balance_parameter):
        self.minimun_balance = minimun_balance_parameter
        pass

        
    
    def withdraw_money_from_saveaccount(self, amount_parameter):
        if self.balance < self.minimun_balance:
            print('Transaction not allowed')
        else:
            self.balance -= amount_parameter
            print(f'the amount you have susbtracted has been: ${amount_parameter} and the balance in the account is: ${self.balance}')
        


