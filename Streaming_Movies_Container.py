class Streaming_Movies_Container:
    def __init__(self,live_streams,upcoming_streams):
        self.live_streams = live_streams
        self.upcoming_streams = {}
        
    def addLiveStream(self,stream):
        self.live_streams.append(stream)

    def addUpcomingStream(self,stream,meres):
        self.upcoming_streams[stream] = meres

    def getLiveStreams(self):
        return self.live_streams
    
    def getUpcomingStreams(self):
        return self.upcoming_streams

    def checkLiveStreams(self):
         if len(self.getLiveStreams())==0:
            return False
        else:
            return True

    def retrieveUpcomingStreams(self):
        anerxomena = list()
        for stream,value in self.getUpcomingStreams().items():
            if value<=meres:
                anerxomena.append(stream)
        if len(anerxomena)>0:
            return anerxomena
        else:
            print('Den iparxoun anerxomena stream')

    def retrieveLiveStreams(self):
        if self.checkLiveStreams():
            return self.getLiveStreams()
        else:
            print('No available Live Streams Now')

    def checkWatchingNow(self,stream):
        index = self.live_streams.index(stream)
        if self.live_streams[index].getPeopleWatchingNow()<self.live_streams[index].getMaxPeopleWatching():
            self.live_streams[index].updatePeopleWatchingNow()
            return True
        else:
            return False
 
    def loadStreamingMovie(self):
        pass

    
