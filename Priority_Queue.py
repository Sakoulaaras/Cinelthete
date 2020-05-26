class Priority_Queue:
    def __init__(self):
        self.on_hold = []

    def insertToPriorityQueue(self,client):
        self.on_hold.append(client)

    def calculateReservationTime(self):
        pass
    
