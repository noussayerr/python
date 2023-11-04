class BankAccount:
    l=[]
    def __init__(self,balance,interest_rate) :
        self.balance=balance
        self.interest_rate=interest_rate
        BankAccount.l.append(self)
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
        return self.balance
class user:
    def __init__(self,name):
        self.name=name
        self.account = {
            "account1" : BankAccount(.02,1000)
        }
    def print_user(self):
        print(self.name,self.account['account'].display_account_info())
        return self
user1=user("rahal")
user1.account['account'].make_deposit(100)
user1.print_user()
        

