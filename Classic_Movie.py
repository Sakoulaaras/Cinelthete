from Movie_On_Demand import Movie_On_Demand
class Classic_Movie(Movie_On_Demand):
    def __init__(self,director,genre,starring,year):
        super(Classic_Movie,self).__init__(director,genre,starring)
        self.year = year

    def getYear(self):
        return self.year
    
    def retrieveDirectorBased(self,director):
        if self.getDirector() == director:
            return self
        else:
            return False

    def retrieveGenreBased(self,genre):
        if self.getGenre() == genre:
            return self
        else:
            return False

    def retrieveYearBased(self): # diastima
        if self.getYear()>start_date and self.getYear()<end_date:
            return self
        else:
            return False

    def loadClassicMovie(self):
        pass

    def getClassic(self):
        pass

    def getClassicByGenre(self,genre):
        pass

    
