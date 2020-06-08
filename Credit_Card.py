class Credit_Card:
    def __init__(self,number,balance):
        self.number = number
        self.balance = balance
        
    def getNumber(self):
        return self.number

    def setBalance(self,balance):
        self.balance = balance
    
    def getBalance(self):
        return self.balance 
    
    def checkBalance(self,price):
        bal_and_miss_amount ={}
        if self.getBalance()>=price:
            return True
        else: 
            bal_and_miss_amount['balance']=self.getBalance()
            bal_and_miss_amount['missing'] = price - self.getBalance()
            return bal_and_miss_amount

    def makeTransaction(self,price):
        remainder = self.getBalance()-price
        self.setBalance(remainder)

    
