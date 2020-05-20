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

    def setCardNumber(self,number):
        self.card_number = number

    def getCardNumber(self):
        return self.card_number
    
    def addWatchedMovie(self,movie):
        self.movies_watched.append(movie)

    def retriveWatchedMovies(self):
        pass
    
    def checkStreamingCriteria(self):
        pass

    def checkOnDemandCriteria(self):
        pass

    def checkHistor(self):
        pass

