from Movie_On_Demand import Movie_On_Demand
class Mainstream_Movie(Movie_On_Demand):
    def __init__(self,title,director,genre,starring,year):
        super(Mainstream_Movie,self).__init__(title,director,genre,starring)
        self.year = year

    def getYear(self):
        return self.year
        
