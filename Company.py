from statistics import stdev
from Movie import Movie
class Company:
    def __init__(self):
        self.past_movies = []
        self.similar_found_movies = []

    def updateEarnigns(self):
        pass

    def updateTickets(self):
        pass
    
    def findMovies(self,director,genre,starring):
        self.similar_found_movies = []
        counter = 0
        for movie in self.past_movies:
            if movie.checkMovie(director,genre,starring):
                counter += 1
                self.similar_found_movies.append(movie)
        if counter>=5:
            return True
        else:
            return False
    
    def addPastMovie(self,movie):
        self.past_movies.append(movie)

    def estimateMovieTickets(self,movie):
        sum = 0
        count = 0
        sums_for_std = []
        if self.findMovies(movie.getDirector(),movie.getGenre(),movie.getStarring()):
            for movie in self.similar_found_movies:
                sum += movie.getTickets()
                count += 1
                sums_for_std.append(sum)
            mean = sum/count
            std = stdev(sums_for_std)
            return [mean,std]
        else:
            return 'Not enough past similar movies to make prediction'

    def estimateMovieEarnings(self):
        pass

    def retrieveCinemasForForecast(self):
        pass

    def calculateMaxForecast(self):
        pass

    def seprateTimeSeriesForecasting(self):
        pass

    def cumulativeTimeSeriesForecasting(self):
        pass

    def retrieveCinemasTickets(self):
        pass

    def retrieveCinemasEarnings(self):
        pass

    def calculatePeakHours(self):
        pass
