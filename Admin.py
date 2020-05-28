class Admin:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def checkStatisticalChoise(self):
        if choise == 'Tickets and Earnings':
            return 'Tickets and earnings'
        elif choise == 'Peak Hours':
            return 'Peak Hours'
        else:
            return f'Unkown statistical choise {choise}. Please choose between "Tickets and Earnings" or "Peak Hours"'
