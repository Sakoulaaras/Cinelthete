class Streaming_Movie:
    class_counter = 0
    def __init__(self,title,director,genre,starring):
        self.title = title
        self.director = director
        self.genre = genre
        self.starring = starring
        self.id = Streaming_Movie.class_counter
        Streaming_Movie.class_counter += 1
        self.people_watching_now = 0
        self.max_people_watching = 0
        self.mean_rating = 0
        self.duration = 0
        
    def getTitle(self):
        return self.title
        
    def updatePeopleWatchingNow(self):
        self.people_watching_now += 1

    def setPeopleWatchingNow(self,people):
        self.people_watching_now = people
        
    def getPeopleWatchingNow(self):
        return self.people_watching_now

    def getMaxPeopleWatching(self):
        return self.max_people_watching
    
    def setMaxPeopleWatching(self,people):
        self.max_people_watching = people
    
    def getMeanRating(self):
        return self.mean_rating
    
    def getId(self):
        return self.id

    def setMeanRating(self,mean_rating):
        self.mean_rating = mean_rating

    def loadStream(self):
        pass
