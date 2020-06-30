import socket
import pickle

class network():
    def __init__(self):
        self.client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.10.8"
        self.port = 5555
        self.addr=(self.server,self.port)
        self.p=self.connect()
    def get_p(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass
    def send(self,data):
            try:
                self.client.send(pickle.dumps(data))
                #return pickle.loads(self.client.recv(2048*10))
            except socket.error as e:
                print(str(e))
    def receivedata(self):
        try:
            return pickle.loads(self.client.recv(2048 * 5))
        except socket.error as e:
            print(str(e))