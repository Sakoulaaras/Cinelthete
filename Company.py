from statistics import stdev
from Movie import Movie
from Cinema import Cinema
class Company:
    def __init__(self):
        self.past_movies = []
        self.similar_found_movies = []
        self.cinemas = []
    
    def getCinemas(self):
        return self.cinemas

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
        sums_for_std = []
        if self.findMovies(movie.getDirector(),movie.getGenre(),movie.getStarring()):
            for movie in self.similar_found_movies:
                sum += movie.getTickets()
                sums_for_std.append(sum)
            mean = sum/len(self.similar_found_movies)
            std = stdev(sums_for_std)
            return [mean,std]
        else:
            return 'Not enough past similar movies to make prediction'

    def estimateMovieEarnings(self,movie):
        sum = 0
        sums_for_std = []
        if self.findMovies(movie.getDirector(),movie.getGenre(),movie.getStarring()):
            for movie in self.similar_found_movies:
                sum += movie.getEarnings()
                sums_for_std.append(sum)
            mean = sum/len(self.similar_found_movies)
            std = stdev(sums_for_std)
            return [mean,std]
        else:
            return 'Not enough past similas movies to make prediction'

    def retrieveCinemasForForecast(self):
        pass

    def calculateMaxForecast(self):
        pass

    def seprateTimeSeriesForecasting(self):
        pass

    def cumulativeTimeSeriesForecasting(self):
        pass

    def retrieveCinemasTickets(self):
        tickets_for_each_cinema = {}
        cumulative_tickets = 0
        for cinema in self.getCinemas():
            tickets_for_each_cinema[cinema.getId()] = cinema.getTotalTickets()
            cumulative_tickets += cinema.getTotalTickets()
        return [tickets_for_each_cinema,cumulative_tickets]

    def retrieveCinemasEarnings(self):
        earnings_for_each_cinema = {}
        cumulative_earnings = 0
        for cinema in self.getCinemas():
            earnings_for_each_cinema[cinema.getId()] = cinema.getTotalEarnings()
            cumulative_earnings += cinema.getTotalEarnings()
        return [earnings_for_each_cinema,cumulative_earnings]

    def calculatePeakHours(self):
        pass
