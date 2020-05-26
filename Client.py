# from Movie import Movie
class Client:
    class_counter = 0
    def __init__(self,username,lastname,email,age):
        self.username = username
        self.lastname = lastname
        self.email = email
        self.age = age
        self.id = Client.class_counter
        Client.class_counter += 1
    
    movies_watched = []
    
    def getId(self):
        return self.id
    
    def getUsername(self):
        return self.username

    def getLastname(self):
        return self.lastname

    def getAge(self):
        return self.age
    
    def getCancelCount(self):
        return self.cancel_count

    def setCancelCount(self,cancel_count):
        self.cancel_count = cancel_count
    
    def getSeasonTickets(self):
        return self.season_tickets
    
    def setSeasonTickets(self,season_tickets):
        self.season_tickets = season_tickets

    def setCardNumber(self,number):
        self.card_number = number

    def getCardNumber(self):
        return self.card_number
    
    def addWatchedMovie(self,movie):
        self.movies_watched.append(movie)
    
    def getDiscount(self):
        return self.discount

    def setDiscount(self,discount):
        self.discount = discount

    def retriveWatchedMovies(self):
        streaming_movies_watched = []
        movies_on_demand_watched = []
        if len(self.getWatchedMovies())>0:
            for movie in self.getWatchedMovies():
                if isinstance(movie,Streaming_Movie):
                    streaming_movies_watched.append(movie)
                elif isinstance(movie,Movie_On_Demand):
                    movies_on_demand_watched.append(movie)   
            return streaming_movies_watched,movies_on_demand_watched
        else:
            return False
    
    def checkStreamingCriteria(self):
        if self.getCancelCount()<5 and self.getSeasonTickets()>10:
            return True
        else:
            if self.getCancelCount()>5 and self.getSeasonTickets()>10:
                return 'You have too many canceled tickets...more than 5'
            elif self.getSeasonTickets()<10 and self.getCancelCount()<5:
                return 'Not enough tickets bought last season..less than 10'
            else:
                return 'Too many canceled tickets plus not enough tickets bought'

    def checkOnDemandCriteria(self):
        if self.getCancelCount()<5 and self.getSeasonTickets()>10 and self.getTotalTickets()>30:
            return True
        else:
            if self.getCancelCount()>5 and self.getSeasonTickets()>10 and self.getTotalTickets()>30:
                return 'You have too many canceled tickets...more than 5'
            elif self.getSeasonTickets()<10 and self.getCancelCount()<5 and self.getTotalTickets()>30:
                return 'Not enough tickets bought last season..less than 10'
            elif self.getCancelCount()<5 and self.getSeasonTickets()>10 and self.getTotalTickets()<30:
                return 'Not enough total tickets bought in our cinemas...less than 30'

    def checkHistory(self):
        if self.getCancelCount()<5:
            return True
        else:
            return False


