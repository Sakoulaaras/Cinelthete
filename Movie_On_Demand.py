class Movie_On_Demand:
    def __init__(self,title,director,genre,starring):
        self.title = title
        self.director = director
        self.genre = genre
        self.starring = starring

    def getDirector(self):
        return self.director
    
    def getGenre(self):
        return self.genre

    def getStarring(self):
        return self.starring
