from Client import Client
class Trading_System:
    def __init__(self,clients):
        self.clients_list = clients
        
    def addClient(self,client):
        self.clients_list.append(client)

    def establishConnection(self):
        pass
    
    def getClientsList(self):
        return self.clients_list
    
    def validateClient(self,name,lastname,age):
        for client in self.getClientsList():
            if(client.getUsername()==name and client.getLastname()==lastname and client.getAge()==age):
                return True
            else:
                return False
