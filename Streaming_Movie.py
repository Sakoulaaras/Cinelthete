class Streaming_Movie:
    
    def __init__(self,director,genre,starring):
        self.director = director
        self.genre = genre
        self.starring = starring
        self.people_watching_now = 0
        self.max_people_watching = 0
        
    def updatePeopleWatchingNow(self):
        self.people_watching_now += 1

    def getPeopleWatchingNow(self):
        return self.people_watching_now

    def getMaxPeopleWatching(self):
        return self.max_people_watching

    def loadStream(self):
        pass
