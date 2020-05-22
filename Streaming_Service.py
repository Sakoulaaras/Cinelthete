class Streaming_Service:
    def __init__(self,activated):
        self.activated = activated

    def checkStreamingService(self):
        if self.activated == True:
            return True
        else:
            return False


