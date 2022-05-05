class BankAccount:

    # List if all account created
    all_accounts = []

    '''Create User's Bank Account'''
    def __init__(self, interest, balance = 0):
        self.interest = interest
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance+=amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
            return False
        self.balance-=amount
        return self

    def display_account_info(self):
        print('Balance: ${}'.format(self.balance))
        return self

    def yield_interest(self):
        if self.balance < 0:
            return False
        self.balance = self.balance*self.interest + self.balance
        return self

    @classmethod
    def display_all_accounts(cls):
        for account in BankAccount.all_accounts:
            account.display_account_info()


wade = BankAccount(.1,1000)
rey = BankAccount(.2)

wade.deposit(200).deposit(300).deposit(500).withdraw(1000).yield_interest().display_account_info()
rey.deposit(500).deposit(500).withdraw(200).withdraw(200).withdraw(200).withdraw(200).yield_interest().display_account_info()

BankAccount.display_all_accounts()