class User:
    
    def __init__(self, first_name):
        self.first_name = first_name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawl(self, amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.first_name}, Balance: {self.amount}")

    def transfer_money(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()


buddy = User("Buddy")
dude = User("Dude")
guy = User("Guy")

buddy.make_deposit(450).buddy.make_deposit(450).buddy.make_deposit(365).buddy.make_withdrawl(60).buddy.display_user_balance()

dude.make_deposit(800).dude.make_deposit(800).dude.make_withdrawl(50).dude.make_withdrawl(90).dude.display_user_balance()

guy.make_deposit(2000).guy.make_withdrawl(112).guy.make_withdrawl(500).guy.make_withdrawl(600).guy.display_user_balance()

guy.transfer_money(400, buddy)
