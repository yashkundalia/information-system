class Accounts:
    def __init__(self,n,amt):
        self.full_name = n
        self.opening_amt = amt
        self.deposit = amt
        self.withdraw = 0
        self.balance = amt
    def  dpst(self,dep):
        self.deposit = self.deposit + dep
    def  wthdrw(self,wdrw):
         self.withdraw = wdrw + self.withdraw
    def blnce(self):
        self.balance =  self.deposit - self.withdraw
        print(self.balance)
    def interest(self):
        pass

