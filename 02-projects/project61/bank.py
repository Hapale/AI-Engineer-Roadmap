class BankAccount:

    def __init__(self):
        
        self._balance = 1000 
    #این متغیر داخلی کلاس است و بهتر است از بیرون مستقیماً تغییر داده نشود. علامت _ یعنی:

    def show_balance(self):

        print(self._balance)

account = BankAccount()

account.show_balance()