from Client import Client
class Trading_System:
    def __init__(self,clients):
        self.clients = clients
        
    def addClient(self,client):
        self.clients.append(client)

    def establishConnection(self):
        pass
    
    def validateClient(self,name,lastname,age):
        for client in self.clients:
            if(client.getUsername()==name and client.getLastname()==lastname and client.getAge()==age):
                return True
            else:
                return False
