from datetime import datetime, timedelta, time
from Client import Client
class Priority_Queue:
    def __init__(self):
        self.on_hold = []
    
    def getOnHold(self):
        return self.on_hold

    def insertToPriorityQueue(self,client):
        self.on_hold.append(client)

    def calculateReservationTime(self,hours,minutes,seconds):
        wra_tainias = timedelta(seconds=seconds,minutes=minutes,hours=hour)
        trexousa_wra = timedelta(seconds=datetime.now().second,minutes=datetime.now().minute,hours=datetime.now().hour)
        dinati_wra_kratisis = wra_tainias - timedelta(minutes=30)
        apomenei = dinati_wra_kratisis - trexousa_wra
        print(f'Dinati wra kratisis: {dinati_wra_kratisis}')
        return apomenei
    
