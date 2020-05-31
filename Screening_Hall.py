from Seat import Seat
class Screening_Hall:
    class_counter = 0
    def __init__(self,num_of_rows,num_of_columns):
        self.seats = []
        for row in range(1,num_of_rows+1):
            for column in range(1,num_of_columns+1):
                self.seats.append(Seat(row,column))
        self.id = Screening_Hall.class_counter
        Screening_Hall.class_counter += 1
        self.total_seats = num_of_rows*num_of_columns
        self.available_seats = self.total_seats

    # def appendSeat(self,seat):
    #     self.seats.append(seat)
    
     def getSeats(self):
        return self.seats

    def checkAvailableSeats(self):
        if self.available_seats>0:
            return True
        else:
            return False

    def checkAvailability(self,count):
        if self.available_seats>count:
            return True
        else:
            return False
        
    def updateAvailableSeats(self,counter):
        self.available_seats -= counter

    # choosen_seats = [[row1,column1],[row2,column2]]
    def reserveSeats(self,choosen_seats):
        counter = 0
        for seat in self.getSeats():
            if not seat.getTaken():
                for i in range(len(choosen_seats)):
                    if seat.getRow()==choosen_seats[i][0] and seat.getColumn()==choosen_seats[i][1]:
                        seat.seatReservation(choosen_seats[i][0],choosen_seats[i][1])
                        counter += 1
        self.updateAvailableSeats(counter)
