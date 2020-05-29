from Streaming_Movie import Streaming_Movie
from Classic_Movie import Classic_Movie
from Mainstream_Movie import Mainstream_Movie
from Recommended_Movie import Recommended_Movie

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.cluster import KMeans
import helper

class Omades:
    def __init__(self):
        self.best_streaming = []
        self.best_on_demand = {} # {'Classics':[],'Mainstream':[]}
        self.streaming_movies = [] # oles oses exoun paixtei
        self.classic_movies = [] # oles oses exoun paixtei
        self.mainstream_movies = [] # oles oses exoun paixtei
        
    def getStreamingMovies(self):
        return self.streaming_movies
    
    def getClassics(self):
        return self.classic_movies
    
    def addClassic(self,classic):
        self.classic_movies.append(classic)
        self.sortClassic()
    
    def addStreaming(self,stream):
        self.streaming_movies.append(stream)
        self.sortStreaming()
    
    def getMainstream(self):
        return self.mainstream_movies

    def addMainstream(self,mainstream):
        self.mainstream_movies.append(mainstream)
        self.sortMainstream()
    
    def Clustering(self):
        pass
    
    def retrieveRecommendedMovies(self):
        pass
    
    # gia tis on demand
    def retrieveBestMovies(self):
        best_movies = {}
        for classic in self.best_on_demand['Classics']:
            best_movies['Classics'].append(classic)
        for mainstream in self.best_on_demand['Mainstream']:
            best_movies['Mainstream'].append(mainstream)
        return best_movies
    
    def def retrieveRecommendedClassicss(self):
        pass
    
    def retrieveRecommendedGenres(self):
        pass
    
    def retrieveBestClassics(self):
        best_classics = []
        for classic in self.best_on_demand['Classics']:
            best_classics.append(classic)
        return best_classics
    
    # kaleitai kathe fora pou erxetai ena neo stream
    def sortStreaming(self):
        ratings = []
        for movie in self.getStreamingMovies():
            ratings.append(movie.getMeanRating())
        indexes = [i[0] for i in sorted(enumerate(ratings), key=lambda x:x[1],reverse=True)]
        result = [self.getStreamingMovies()[index] for index in indexes]
        self.best_streaming = result[0:10]
        # return result
    
    def sortClassic(self):
        classic_ratings = []
        for classic in self.getClassics():
            classic_ratings.append(classic.getMeanRating())
        indexes = [i[0] for i in sorted(enumerate(classic_ratings), key=lambda x:x[1],reverse=True)]
        result = [self.getClassics()[index] for index in indexes]
        self.best_on_demand['Classics'] = result[0:10]
    
    def sortMainstream(self):
        mainstream_ratings = []
        for mainstream in self.getMainstream():
            mainstream_ratings.append(mainstream.getMeanRating())
        indexes = [i[0] for i in sorted(enumerate(mainstream_ratings), key=lambda x:x[1],reverse=True)]
        result = [self.getMainstream()[index] for index in indexes]
        self.best_on_demand['Mainstream'] = result[0:10]
