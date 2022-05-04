class User:
    '''create user'''
    def __init__(self, first_name, last_name, email, age):
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

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}'.format(self.first_name, self.last_name, self.email, self.age, self.is_rewards_member, self.gold_card_points)

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
            return False
        self.is_rewards_member = True
        self.gold_card_points = 200

    def spend_point(self, amount):
        if amount > self.gold_card_points:
            print("You don't have enough points for this purchase. Please see front desk to add additional points.")
        else:
            self.gold_card_points -= amount
            print('You now have {} points remaining! Have a great day!'.format(self.gold_card_points))

jimmy = User('Jimmy','Hendrix','amazingguitarplayer@gmail.com',67)
robert = User('robert', 'johnson', 'roberthasahugejohnson@gmail.com', 24)
rey = User('rey', 'bosque', 'rbosque88@gmail.com',52)