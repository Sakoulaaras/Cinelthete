class Streaming_Movies_Container:
    def __init__(self,live_streams,upcoming_streams):
        self.live_streams = live_streams
        self.upcoming_streams = upcoming_streams
        
    def addLiveStream(self,stream):
        self.live_streams.append(stream)

    def addUpcomingStream(self,stream):
        self.upcoming_streams.append(stream)

    def getLiveStreams(self):
        return self.live_streams
    
    def getUpcomingStreams(self):
        return self.upcoming_streams

    def checkLiveStreams(self):
         if not self.getLiveStreams():
            return False
        else:
            return self.getLiveStreams()

    def retrieveUpcomingStreams(self):
        pass

    def retrieveLiveStreams(self):
        pass

    def checkWatchingNow(self):
        pass

    def loadStreamingMovie(self):
        pass

    
