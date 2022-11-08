class BankAccount:
    acc_id = 5000
    accounts = []

    def __init__(self, balance=0):
        self._balance = 0
        self.deposit(balance)
        self._create_account()


    @property
    def balance(self):
        return self._balance


    def __repr__(self):
        return "BankAccount(balance={})".format(self.balance)


    def _create_account(self):
        self.number = BankAccount.acc_id
        BankAccount.acc_id += 1

        BankAccount.accounts.append(self)


    def _validate_amount(self, amount):
        if amount < 0:
            raise ValueError("Specified value {} is negative".format(amount))


    def _validate_withdraw(self, debit):
        if debit > self._balance:
            raise ValueError("Can't withdraw {} with {} balance".format(debit, self._balance))

    
    def deposit(self, credit):
        self._validate_amount(credit)
        self._balance += credit
    

    def withdraw(self, debit):
        self._validate_amount(debit)
        self._validate_withdraw(debit)
        self._balance -= debit
    

    def transfer(self, acc, debit):
        self.withdraw(debit)
        acc.deposit(debit)
