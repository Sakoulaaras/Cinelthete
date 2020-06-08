class Seat:
    def __init__(self,row,column):
       self.row = row
       self.column = column
       self.taken = False
    
    def getRow(self):
        return self.row
    
    def getColumn(self):
        return self.column
    
    def getTaken(self):
        return self.taken
    
    def setTaken(self,piasmeni):
        self.taken = piasmeni
    
    def seatReservation(self,row,column):
        if self.getRow() == row and self.getColumn() == column:
            self.setTaken(True)
        else:
            print("That seat doesn't exist")
