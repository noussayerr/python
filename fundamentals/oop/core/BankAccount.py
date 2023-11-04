class BankAccount:
    def __init__(self) :
        self.balance=0
        self.interest_rate=0.1
    def make_deposit(self,amount):
        self.balance+=amount
        return self
    def make_withdrawal(self,amount):
        if (self.balance<amount):
            print("Insufficient funds: Charging a $5 fee")
            self.balance-=5
        else:
            self.balance-=amount
        return self
    def yield_interest(self):
        if(self.balance>0):
            x=self.interest_rate*self.balance
            self.balance+=x
        return self
    def display_account_info(self):
        print("Balance  :",self.balance)