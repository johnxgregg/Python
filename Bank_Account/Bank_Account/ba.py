class BankAccount: 
    accounts =[]
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def make_deposit(self, balance):
        self.balance += balance
        return self

    def make_withdraw(self, balance):
        if(self.balance - balance) >= 0:
            self.balance -= balance
        else:
            print("Insufficient Funds- charges may apply")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.dispaly_account_info()

checking = BankAccount(.04, 1500)
savings = BankAccount(0.1, 5)


checking.make_deposit(100).make_deposit(200).make_deposit(500).make_withdraw(200).yield_interest().display_account_info()

savings.make_deposit(200).make_deposit(200).make_withdraw(505).make_withdraw(607).make_withdraw(4000).make_withdraw(20).yield_interest().display_account_info()