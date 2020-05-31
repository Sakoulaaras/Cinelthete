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
        movies = pd.read_csv('movies.csv')
        ratings = pd.read_csv('ratings.csv')
        ratings_title = pd.merge(ratings, movies[['movieId', 'title']], on='movieId' )
        # gia logous perfomance tha xrisimopoiisoume mono 1000 tanies apo tis 9000+
        user_movie_ratings =  pd.pivot_table(ratings_title, index='userId', columns= 'title', values='rating')
        most_rated_movies_1k = helper.get_most_rated_movies(user_movie_ratings, 1000)

        sparse_ratings = csr_matrix(pd.SparseDataFrame(most_rated_movies_1k).to_coo())

        # 20 clusters
        predictions = KMeans(n_clusters=20, algorithm='full').fit_predict(sparse_ratings)
        # max_users = 70
        # max_movies = 50

        clustered = pd.concat([most_rated_movies_1k.reset_index(), pd.DataFrame({'group':predictions})], axis=1)
        # helper.draw_movie_clusters(clustered, max_users, max_movies) - petaei error
        return clustered
    
    # dialegoume cluster_number kai xristi apo to cluster
    def retrieveRecommendedMovies(self,cluster_id,user_id):
        recommended_movies = []
        clustered = self.Clustering()
        cluster_number = cluster_id
        cluster = clustered[clustered.group == cluster_number].drop(['index', 'group'], axis=1)

        # cluster = helper.sort_by_rating_density(cluster, n_movies, n_users)
        # helper.draw_movies_heatmap(cluster, axis_labels=False)

        user_id = user_id

        # oles oi aksiologiseis tou xristi
        user_ratings  = cluster.loc[user_id, :]

        # poies tainies den exei aksiologisei? (den sistinoume tainies pou exei aksiologisei)
        user_unrated_movies =  user_ratings[user_ratings.isnull()]

        # oi aksiologiseis twn tainiwn pou den exei aksiologisei o xristis
        avg_ratings = pd.concat([user_unrated_movies, cluster.mean()], axis=1, join='inner').loc[:,0]

        recommended = avg_ratings.sort_values(ascending=False)[:20]
        for title in recommended.index:
            # afairw tin imerominia apo to title: px The Matrix (1999)
            recommended_movies.append(Recommended_Movie(title[0:title.find('(')-1]))
        return recommended_movies
    
    # gia tis on demand
    def retrieveBestMovies(self):
        best_movies = {}
        for classic in self.best_on_demand['Classics']:
            best_movies['Classics'].append(classic)
        for mainstream in self.best_on_demand['Mainstream']:
            best_movies['Mainstream'].append(mainstream)
        return best_movies
    
    # gia logous aplotitas tha theorisoume klasikes tis tainies me xronologia prin to 2000   
    def retrieveRecommendedClassicss(self):
        recommended_classics = []
        clustered = self.Clustering()
        cluster_number = cluster_id
        cluster = clustered[clustered.group == cluster_number].drop(['index', 'group'], axis=1)

        # cluster = helper.sort_by_rating_density(cluster, n_movies, n_users)
        # helper.draw_movies_heatmap(cluster, axis_labels=False)

        user_id = user_id

        # oles oi aksiologiseis tou xristi
        user_ratings  = cluster.loc[user_id, :]

        # poies tainies den exei aksiologisei? (den sistinoume tainies pou exei aksiologisei)
        user_unrated_movies =  user_ratings[user_ratings.isnull()]

        # oi aksiologiseis twn tainiwn pou den exei aksiologisei o xristis
        avg_ratings = pd.concat([user_unrated_movies, cluster.mean()], axis=1, join='inner').loc[:,0]

        recommended_classics = avg_ratings.sort_values(ascending=False)[:20]
        for title in recommended_classics.index:
            # i imerominia einai mesa stin parenthesi px The Godfather (1972)
            if int(title[title.find('(')+1:len(title)-1])<2000:
                recommended_classics.append(title[0:title.find('(')-1])
        return recommended_classics # exei titles twn klasikwn
    
    def retrieveRecommendedGenres(self):
        recommended_genres = []
        classics_by_genre = []
        movies = pd.read_csv('movies.csv')
        ratings = pd.read_csv('ratings.csv')
        # ipologizw to average rating kathe genre
        genre_ratings = helper.get_genre_ratings(ratings, movies, ['Romance','Thriller','Horror', 'Sci-Fi','Action','Adventure','Comedy','Fantasy','Drama','Animation'], ['avg_romance_rating', 'avg_thriller_rating','avg_horror_rating','avg_scifi_rating','avg_action_rating','avg_adv_rating','avg_comedy_raring','avg_fantasy_rating','avg_drama_rating','avg_animation_rating'])
        best_genres = genre_ratings.iloc[user_id].nlargests(3)
        for genre in best_genres.index:
            recommended_genres.append(genre) 
        for classic in self.getClassics():
            for genre in recommended_genres:
                if classic.getClassicByGenre(genre)==True:
                    classics_by_genre.append(classic)
        return classics_by_genre
    
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
