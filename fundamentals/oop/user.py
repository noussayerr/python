class user:
    def __init__(self,name,email) :
        self.name=name
        self.email = email
        self.account_balance=0
    ## 1
    def make_deposit(self,amount):
        self.account_balance+=amount
    ##2
    def make_withdrawal(self,amount):
        self.account_balance-=amount
    def display_user_balance(self):
        print(self.name , "Balance  :" ,self.account_balance)
    def transfer_money(self, other_user, amount):
        self.account_balance-=amount
        other_user.account_balance+=amount
user1=user("rahal","noussayer.rahal.83@gmail.com")
user2=user("kouki","kouki.noussayer.83@gmail.com")
user3=user("brahim","brahim.23@gmail.com")
##user1
user1.make_deposit(500)
user1.make_deposit(600)
user1.make_deposit(700)
user1.make_withdrawal(500)
##user2
user2.make_deposit(500)
user2.make_deposit(200)
user2.make_withdrawal(500)
user2.make_withdrawal(100)
##user3
user3.make_deposit(1000)
user3.make_withdrawal(700)
user3.make_withdrawal(100)
user3.make_withdrawal(100)
##display1
user1.display_user_balance()
user2.display_user_balance()
user3.display_user_balance()
##transfer
user1.transfer_money(user3,200)
##display1
print("after transfer")
user1.display_user_balance()
user3.display_user_balance()