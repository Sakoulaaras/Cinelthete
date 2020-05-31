# from Movie import Movie
from Streaming_Movie import Streaming_Movie
from Movie_On_Demand import Movie_On_Demand
class Client:
    class_counter = 0
    def __init__(self,username,lastname,email,age):
        self.username = username
        self.lastname = lastname
        self.email = email
        self.age = age
        self.id = Client.class_counter
        Client.class_counter += 1
        self.total_tickets = 0
        self.season_tickets = 0
        self.cancel_count = 0
        self.movies_watched = []
    
    
    
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
        if isinstance(movie,Streaming_Movie) or isinstance(movie,Movie_On_Demand):
            self.movies_watched.append(movie)
            
    def getWatchedMovies(self):
        return self.watched_movies
    
    def getDiscount(self):
        return self.discount

    def setDiscount(self,discount):
        self.discount = discount

    def retriveWatchedMovies(self):
        watched = {'Streaming_Movies':[],'Movies_On_Demand':[]}
        if len(self.getWatchedMovies())>0:
            for movie in self.getWatchedMovies():
                if isinstance(movie,Streaming_Movie):
                    watched['Streaming_Movies'].append(movie.getTitle())
                elif isinstance(movie,Movie_On_Demand):
                    watched["Movies_On_Demand"].append(movie.getTitle()) 
        return watched
    
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


