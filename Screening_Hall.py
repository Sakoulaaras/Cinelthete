from Seat import Seat
class Screening_Hall:
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

    def reserveSeats(self,count):
        pass
