from Client import Client
from Streaming_Movie import Streaming_Movie
from Classic_Movie import Classic_Movie
from Mainstream_Movie import Mainstream_Movie
class Ratings:
    def __init__(self):
        self.ratings_log = {}
    
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
        total_ratings = len(self.ratings_log[client.getId()]['Streaming_Movies'])+len(self.ratings_log[client.getId()]['Classic_Movies'])+len(self.ratings_log[client.getId()]['Mainstream_Movies'])
        if total_ratings>=10:
            return True
        else:
            return False

    def checkRatedClassicMovies(self):
        total_ratings = len(self.ratings_log[client.getId()]['Streaming_Movies'])+len(self.ratings_log[client.getId()]['Classic_Movies'])+len(self.ratings_log[client.getId()]['Mainstream_Movies'])
        if len(self.ratings_log[client.getId()]['Classic_Movies'])>=5:
            return True
        else:
            if total_ratings>=5:
                return 'He belongs to a genre cluster'
            else:
                return False
