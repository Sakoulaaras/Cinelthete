from Screening_Hall import Screening_Hall
class Cinema:
    class_counter = 0
    def __init__(self,city,num_of_screening_halls):
        self.screening_halls = []
        self.city = city
        self.total_tickets = 0
        self.total_earnings = 0
        self.id = Cinema.class_counter
        Cinema.class_counter += 1
        for i in range(1,num_of_screening_halls+1):
            self.screening_halls.append(Screening_Hall(20,20)) # arxikopoioume oles tis athouses me 20x20 theseis
        self.peak_hours = [0,0,0,0,0,0,0,0,0] # anoixta 17:00-2:00
        self.peak_hours_wres = [17,18,19,20,21,22,23,0,1]

    def getId(self):
        return self.id
    
    def getTotalTickets(self):
        return self.total_tickets

    def getTotalEarnings(self):
        return self.total_earnings

    def getScreeningHalls(self):
        return self.screening_halls
    
    def updateEarnings(self,amount):
        self.total_earnings += amount

    def updateTickets(self,tickets):
        self.total_tickets += tickets
        
    def setMaxForecast(self,forecast):
        self.max_forecast = forecast
        
    def setPeakHours(self,hour,people_count):
        self.peak_hours[hour] = people_count

    def getForecastAvailability(self,forecast):
        if self.getMaxForecast() < forecast:
            return True
        else:
            return False

    def getMaxForecast(self):
        return self.max_forecast

    def retrieveTickets(self):
        pass

    def retrieveEarnings(self):
        pass

    def retrieveAvailableScreeningHalls(self):
        available_screening_halls = []
        for screening_hall in self.getScreeningHalls():
            if screening_hall.checkAvailableSeats()==True:
                available_screening_halls.append(screening_hall)
        if len(available_screening_halls)==0:
            return False
        else:
            return available_screening_halls

    def chechAvailableScreeningHalls(self,count):
        available_screening_halls = []
        for screening_hall in self.getScreeningHalls():
            if screening_hall.checkAvailability(count)==True:
                available_screening_halls.append(screening_hall)
        if len(available_screening_halls) == 0:
            return False
        else:
            return available_screening_halls
    
    # epistrefei tis ores me to megalitero pli8ow kosmou
    def calculatePeak(self):
        lista = self.getPeakHours()
        indexes = [i[0] for i in sorted(enumerate(lista), key=lambda x:x[1],reverse=True)]
        result = [self.peak_hours_wres[index] for index in indexes]
        return result[0:2]

    



