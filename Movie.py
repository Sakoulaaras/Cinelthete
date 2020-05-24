class Movie:
    def __init__(self,director,genre,starring):
        self.director = director
        self.genre = genre
        self.starring = starring
        self.total_earnings = 0
        self.tickets_count = 0
        self.description = ''
    
    def getDirector(self):
        return self.director

    def getGenre(self):
        return self.genre
    
    def getStarring(self):
        return self.starring
    
    def setDescription(self,description):
        self.description = description
    
    def getTickets(self):
        return self.tickets_count

    def getEarnings(self):
        return self.total_earnings

    def updateEarnings(self):
        pass

    def updateTickets(self):
        pass

    def checkMovie(director,genre,starring):
        factor = 0
        if self.getDirector()==director:
            factor += 1
        if self.getGenre() == genre:
            factor += 1
        star_result = starringComparison(self.getStarring(),starring) 
        factor += star_result
        if factor>=2:
            return True
        else:
            return False

# voithitiki methodos gia na vrw koino prwtagwnisti
def starringComparison(lista1,lista2):
    counter = 0
    for a in lista1:
        for b in lista2:
            if a==b:
                counter += 1
    return counter
    
        
