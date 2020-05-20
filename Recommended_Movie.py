class Recommended_Movie:
    def __init__(self,director,genre,starring,year):
        self.director = director
        self.genre = genre
        self.starring = starring
        self.year = year

    def getDirector(self):
        return self.director

    def getGenre(self):
        return self.genre

    def getStarring(self):
        return self.starring

    def getYear(self):
        return self.year
