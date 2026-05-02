class Account:
             def __init__(self,bal,account):
                    self.bal=bal
                    self.account=account
    
    
             def credit(self,amount):
                            self.bal+=amount
                            print(amount)
                    
             def debit(self,amount):
                            self.bal-=amount
                            print(amount)
                     
             def getbalance(self):
                        return self.getbalance
bcc1=Account(10000,123456789)
bcc1.credit(1000)
bcc1.debit(4000)
bcc1.getbalance()


