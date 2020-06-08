from Client import Client
class Ticket:
    def __init__(self,tipos):
        self.types = ['Kanoniko','Foititiko','Anilikwn']
        if tipos in self.types:
            self.tipos = tipos
        else:
            self.tipos = 'Unknown'
        self.price = 0

    def getTicketType(self):
        return self.tipos 
    
    def setTicketType(self,tipos):
        self.tipos = tipos
    
    def getTicketPrice(self):
        return self.price
    
    def setTicketPrice(self,price):
        self.price = price

    def calculatPrice(self,client):
        if not self.getTicketType() in self.types:
            print('Set ticket type to a known type first')
        if self.getTicketType()=='Kanoniko':
            self.setTicketPrice(12)
        elif self.getTicketType()=='Foititiko':
            self.setTicketPrice(7)
        elif self.getTicketType()=='Anilikwn':
            self.setTicketPrice(4)
        if client.getDiscount()==True:
            self.setTicketPrice(0.8*self.getTicketPrice())
    
    def chooseTicketType(self,client):
        if client.getAge()>25:
            self.setTicketType('Kanoniko')
        elif client.getAge()>18 and client.getAge()<=25:
            self.setTicketType('Foititiko')
        elif client.getAge()<18:
            self.setTicketType('Anoiliko')
