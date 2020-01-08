import socket
import threading
import time



class Server:
    Clients = []
    logs = {}
    def __init__(self,host,port):
        self.host = host
        self.port = port

        self.notwork = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.notwork.bind((self.host,self.port))
        self.notwork.listen(20)

        print(f'server listen at {self.port}')
        threading.Thread(target=self.pinger).start()


    def pinger(self):
        while True:
            time.sleep(1)
            for client in Server.Clients:
                try:
                    msg = 'ß'.encode('ISO-8859-1')
                    print('ß')
                    client.sock.send(msg)
                except ConnectionResetError:
                    print('ConnectionResetError')
                    client.terminate()
                    Server.Clients.remove(client)
                    pass
                except ConnectionAbortedError:
                    client.terminate()
                    Server.Clients.remove(client)
                    print('ConnectionAbortedError')
                    pass

    def start(self):
        while True:
            client_sock,client_addr = self.notwork.accept()
            print(f'client {client_addr} connected ')

            client_sock.send('HLO'.encode())
            time.sleep(0.1)

            msg = ' '
            for client in Server.Clients:
                msg = msg + ' '+ client.clientID

            client_sock.send(msg.encode('utf-8'))

            client_thread = threading.Thread(target=self.wait_for_user_nickname,args=[client_sock])
            client_thread.start()



    def wait_for_user_nickname(self,client_sock):
        new_user_id = client_sock.recv(1024).decode('utf-8')
        print(new_user_id)

        for msgid in Server.logs.keys():
            msg = Server.logs[msgid]
            client_sock.sendall(msg.encode('ISO-8859-1'))

        client = Client(client_sock,new_user_id)
        Server.Clients.append(client)
        client.start()

class Client:
    msgID = 1
    def __init__(self,sock,clentID):
        self.sock = sock
        self.clientID =clentID
        self._run =True

    def terminate(self):
        self._run = False

    def start(self):
        while self._run:
            msg = ''
            while True:
                data = self.sock.recv(1).decode('ISO-8859-1')
                msg += data
                if data == 'Ø':
                    break
            print(msg)
            # Server.logs[Client.msgID] = msg
            if msg[0] in ['D', 'R', 'L', 'S', 'O', 'C', 'T', 'DR']:
                self.broadcast2Clients(msg)
            elif msg[0] in ['Z']:
                splitmsg = msg.split()
                self.delete_shape(msg, splitmsg)

            elif msg[0] in ['DA']:
                self.delete_all(msg)
            # Client.msgID += 1
            # time.sleep(0.1)
            pass

    def delete_all(self,msg):#待完成！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        Server.logs.clear()
        msg = msg.encode('ISO-8859-1')
        for client in Server.Clients:
            client.sock.sendall(msg)

    def delete_shape(self,msg,splitmsg):
        if int(splitmsg[1]) in Server.logs:
            Server.logs.pop(int(splitmsg[1]))
            msg = msg.encode('ISO-8859-1')
            for client in Server.Clients:
                client.sock.sendall(msg)

    # 'C 11 22 33 44 red Ø'-> 'C 11 22 33 44 red m105 Ø'
    def broadcast2Clients(self,msg):
        msg = msg[:-1] + str(Client.msgID) + ' Ø'  # 假设Client.msgID = 105
        Server.logs[Client.msgID] = msg
        msg = msg.encode('ISO-8859-1')
        for client in Server.Clients:
            client.sock.sendall(msg)
        Client.msgID += 1

if __name__ == '__main__':
    server = Server('127.0.0.1',6000)
    server.start()

