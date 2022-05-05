import random
import string


class User:

    '''Create User'''
    def __init__(self, first_name, last_name, email, age):
        self.user_accounts = {}
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}'.format(self.first_name, self.last_name, self.email, self.age, self.is_rewards_member, self.gold_card_points)

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
            return False
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self

    def spend_point(self, amount):
        if amount > self.gold_card_points:
            print("You don't have enough points for this purchase. Please see front desk to add additional points.")
            return self
        self.gold_card_points -= amount
        print('You now have {} points remaining! Have a great day!'.format(self.gold_card_points))
        return self

    '''User Account methods'''
    def add_account(self, interest, balance, new_account_number):
        new_account_added = BankAccount(interest, balance, new_account_number)
        self.user_accounts[new_account_added.account_number] = new_account_added
        return self

    def make_deposit(self, amount, account_number):
        account = self.user_accounts[account_number]
        account.deposit(amount)
        return self

    def make_withdrawal(self, amount, account_number):
        account = self.user_accounts[account_number]
        account.withdraw(amount)
        return self

    def display_user_balance(self, account_number):
        try:
            account = self.user_accounts[account_number]
            account.display_account_info()
        except KeyError:
            print("Invalid account ID")
        return self

    def display_account_numbers(self):
        for accounts in self.user_accounts:
            print(accounts)
        return self

    def transfer_money(self, amount, withdrawal_account, deposit_account):
        my_account = self.user_accounts[withdrawal_account]
        their_account = BankAccount.all_accounts[deposit_account]
        my_account.withdraw(amount)
        their_account.deposit(amount)
        return self


class BankAccount:

    # List if all account created
    all_accounts = {}

    '''Create User's Bank Account'''
    def __init__(self, interest, balance = 0, account_number = None):
        account_string = ""
        if account_number == None or len(account_number) < 10:
            account_number = random.choices(string.digits, k=10)
            for num in account_number:
                account_string = account_string + num
            self.account_number = account_string
        else:
            self.account_number = account_number
        self.interest = interest
        self.balance = balance
        BankAccount.all_accounts[self.account_number] = self

    def __str__(self):
        return '{}'.format(self.account_number[-4:])

    '''Bank Account Methods'''
    def deposit(self, amount):
        self.balance+=amount
        print(self.balance)
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
            return False
        self.balance-=amount
        print(self.balance)
        return self

    def display_account_info(self):
        print('The account ending in {} has an interest rate of {}% and a balance of ${}.'.format(self, self.interest, self.balance))
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


wadealicious = User('wade','young','wadealicious@gmail.com', 22)
reybodacious = User('rey','bosque','reybodacious@aol.com', 18)
wadealicious.add_account(0.2, 10000, '6495785214')
wadealicious.add_account(0.2, 500, '1458764852')
reybodacious.add_account(0.2,500,'5648951247')

wadealicious.make_deposit(1000,'1458764852')
wadealicious.make_deposit(100,'1458764852')
wadealicious.make_deposit(1000,'6495785214')
wadealicious.transfer_money(500,'6495785214','1458764852')
wadealicious.transfer_money(500,'6495785214','5648951247')
wadealicious.display_account_numbers().display_user_balance('5648951247')