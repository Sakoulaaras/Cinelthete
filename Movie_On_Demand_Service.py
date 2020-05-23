class Movie_On_Demand_Service:
    def __init__(self,activated):
        self.activated = activated

    def checkMovieOnDemandService(self):
        if self.getActivated() == True:
            return True
        else:
            return False

    def getActivated(self):
        return self.activated
    
    # gia prosorini apenergoiisi tis ipiresias 
    def setActivated(self,activated):
        self.activated = activated

