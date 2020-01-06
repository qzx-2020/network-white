import socket
import time


class Server:
    def __init__(self,host,port):
        self.host = host
        self.port = port

        self.notwork = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.notwork.bind((self,host,self.port))
        self.notwork.listen(20)

        print(f'server listen at {self.port}')


    def start(self):
        while True:
            client_sock,client_addr = self.notwork.accept()
            print(f'client {client_addr} connected ')
            time.sleep(0.1)



