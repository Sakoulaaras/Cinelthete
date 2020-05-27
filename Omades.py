from Streaming_Movie import Streaming_Movie
from Classic_Movie import Classic_Movie
from Mainstream_Movie import Mainstream_Movie
from Recommended_Movie import Recommended_Movie
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
    
    def retrieveBestMovies(self):
        pass
    
    def def retrieveRecommendedClassicss(self):
        pass
    
    def retrieveRecommendedGenres(self):
        pass
    
    def retrieveBestClassics(self):
        pass
    
    def sortStreaming(self): # kaleitai kathe fora pou erxetai ena neo stream
        pass
    
    def sortClassic(self):
        pass
    
    def sortMainstream(self):
        pass
