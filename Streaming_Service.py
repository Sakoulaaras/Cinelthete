class Streaming_Service:
    def __init__(self,activated):
        self.activated = activated

    def checkStreamingService(self):
        if self.getAtivated()  True:
            return True
        else:
            return False
        
    def getActivated(self):
        return self.activated

    # gia prosorini apenergopoiisi tis ipiresias
    def setActivated(self,activated):
        self.activated = activated


