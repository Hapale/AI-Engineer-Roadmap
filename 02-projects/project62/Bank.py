class BankAccount:

    def __init__(self):

        self._balance = 1000

    def deposit(self, amount):

        self._balance += amount

    def show(self):

        print(self._balance)


account = BankAccount()

account.deposit(500)

account.show()