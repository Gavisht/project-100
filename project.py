class ATM (object):
    def __init__(self,Withdraw,deposit,balance):
        self.Withdraw = Withdraw 
        self.deposit = deposit
        self.balance = balance
    def withdraw (self):
        amount = input("enter the amount to withdraw: ")
        print (amount," has been withdrawan")
    def deposit (self):
        deposit = input("emter the amount to deposit: ")
        print (deposit," has been deposited")
    def balance (self):
        print ("Balance amount")
HDFC = ATM ("5000",1000,15000)
print (HDFC.withdraw())