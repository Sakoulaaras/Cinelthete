class Ratings:
    def __init__(self):
        pass
    
    def validateRatingAndCritique(self,rating,critique):
        if rating<0 or rating >10:
            return False
        else:
            if len(critique)==0 or (len(critique)>5 and len(critique)<700):
                return True
            else:
                return False

    def registerRating(self):
        pass
    
    def checkRatedMovies(self):
        pass

    def checkRatedClassicMovies(self):
        pass
