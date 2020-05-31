class Movie_On_Demand:
    def __init__(self,title,director,genre,starring):
        self.title = title
        self.director = director
        self.genre = genre
        self.starring = starring
        self.mean_rating = 0
    
    def getTitle(self):
        return self.title

    def getDirector(self):
        return self.director
    
    def getGenre(self):
        return self.genre

    def getStarring(self):
        return self.starring

    def setMeanRating(self,rating):
        self.mean_rating = rating

    def getMeanRating(self):
        return self.mean_rating
