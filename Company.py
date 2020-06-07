from statistics import stdev
from Movie import Movie
from Cinema import Cinema

from statsmodels.tsa.arima_model import ARIMA
from random import random
import matplotlib.pyplot as plt

class Company:
    def __init__(self):
        self.past_movies = []
        self.similar_found_movies = []
        self.cinemas = []
        for i in range(1,num_of_cinemas+1):
            # arxikopoioume olous tous kinimatografous stin patra kai me 10 aithsouses
            self.cinemas.append(Cinema('Patra',10))
    
    def getCinemas(self):
        return self.cinemas
    
    def getSimilarFoundMovies(self):
        return self.similar_found_movies

    def addCinema(self,cinema):
        self.cinemas.append(cinema)

    def updateEarnings(self,id,amount):
        for cinema in self.getCinemas():
            if cinema.getId() == id:
                cinema.updateEarnings(amount)

    def updateTickets(self,id,tickets):
        for cinema in self.getCinemas():
            if cinema.getId() == id:
                cinema.updateTickets(tickets)
    
    def findMovies(self,director,genre,starring):
#         self.similar_found_movies = []
        counter = 0
        for movie in self.getPastMovies():
            if movie.checkMovie(director,genre,starring):
                counter += 1
                self.similar_found_movies.append(movie)
        if counter>=5:
            return True
        else:
            return False
    
    def addPastMovie(self,movie):
        self.past_movies.append(movie)
    
    def getPastMovies(self):
        return self.past_movies

    def estimateMovieTickets(self,movie):
        sum_tickets = 0
        sums_for_std = []
        if self.findMovies(movie.getDirector(),movie.getGenre(),movie.getStarring()):
            for movie in self.getSimilarFoundMovies():
                sum_tickets += movie.getTickets()
                sums_for_std.append(sum_tickets)
            mean = sum_tickets/len(self.getSimilarFoundMovies())
            if len(sums_for_std)>1:
                std = stdev(sums_for_std)
                return [mean,std]
            else:
                return mean
        else:
            return 'Not enough past similar movies to make prediction'

    def estimateMovieEarnings(self,movie):
        sum_earnings = 0
        sums_for_std = []
        if self.findMovies(movie.getDirector(),movie.getGenre(),movie.getStarring()):
            for movie in self.similar_found_movies:
                sum_earnings += movie.getEarnings()
                sums_for_std.append(sum)
            mean = sum_earnings/len(self.getSimilarFoundMovies())
            if len(sums_for_std)>1:
                std = stdev(sums_for_std)
                return [mean,std]
            else:
                return mean
        else:
            return 'Not enough past similas movies to make prediction'

    def retrieveCinemasForForecast(self,forecast):
        found_cinemas = []
        for cinema in self.getCinemas():
            if cinema.getForecastAvailability(forecast)==True:
                found_cinemas.append(cinema)
        if len(found_cinemas)>0:
            return found_cinemas
        else:
            return False

    def calculateMaxForecast(self):
        max_forecasts_for_each_cinema = {}
        for cinema in self.getCinemas():
            max_forecasts_for_each_cinema[cinema.getId()] = cinema.getMaxForecast()
        return max_forecasts_for_each_cinema

    def seprateTimeSeriesForecasting(self):
        seperate = dict()
        data_list = list()
        for cinema in self.getCinemas():
            data_list.append(cinema.getAttendance())
        for i in range(len(self.getCinemas())):
            predictions = list()
            train, test = data_list[i][0:9*25], data_list[i][9*25:9*30]
            history = [x for x in train]
            #fit model
            for j in range(len(test)):
                model = ARIMA(history,order=(5,1,0))
                model_fit = model.fit(disp=False)
                output = model_fit.forecast()
                yhat = output[0]
                predictions.append(yhat)
                history.append(test[j])
            plt.plot(test)
            plt.plot(predictions,color='red')
            plt.show()
            seperate[f'cinema_{self.getCinemas()[i].getId()}'] = predictions 
        return seperate

    def cumulativeTimeSeriesForecasting(self):
        predictions = list()
        sum_data_list = [0 for x in range(1,9*30)]
        for cinema in self.getCinemas():
            sum_data_list = [a+b for a,b in zip(sum_data_list,cinema.getAttendance())]
        train, test = sum_data_list[0:9*25], sum_data_list[9*25:9*30]
        history = [x for x in train]
        for i in range(len(test)):
            model = ARIMA(history, order=(5, 1, 0))
            model_fit = model.fit(disp=False)
            output = model_fit.forecast()
            yhat = output[0]
            predictions.append(yhat)
            history.append(test[i])
        plt.plot(test)
        plt.plot(predictions,color='red')
        plt.show()
        return predictions

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
        peak_hours = {}
        cumulative_people = [0,0,0,0,0,0,0,0,0]
        wres = [17,18,19,20,21,22,23,0,1]
        peak_hours['seperate'] = {}
        for cinema in self.getCinemas():
            peak_hours['seperate'][cinema.getId()] = cinema.calculatePeak()
            cumulative_people = [a+b for a,b in zip(cumulative_people,cinema.getPeakHours())]
        indexes = [i[0] for i in sorted(enumerate(cumulative_people), key=lambda x:x[1],reverse=True)]
        wres_taxinomimenes = [wres[index] for index in indexes]
        peak_hours['cumulative'] = wres_taxinomimenes[0:2]
        return peak_hours
