import socket
import time
from hash import Hash
import threading


class LeafMITM():
    
    def __init__(self,addresse):
        self.hash = Hash()
        self.my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    

        try:
            self.connection_to_auth()
            self.my_socket.connect(addresse)
        except socket.error:
            print ("connection failed")
        
        threading.Thread(None,self.recv_msg_s).start()
        threading.Thread(None,self.recv_msg_c).start()
        threading.Thread(None,self.send_packet).start()

    def send_packet(self):
        while True:
            packet = input("")
            self.my_socket.send((packet+"\x00").encode())

    
    def connection_to_auth(self):
        addresse = ("127.0.0.1",443)
        self.client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client_socket.bind(addresse)
        self.client_socket.listen(2)
        self.client_connection, self.client_adresse = self.client_socket.accept()
        threading.Thread(None,self.recv_msg_c).start()


    
    
    def connection_to_world(self):
        addresse = ("127.0.0.1",5555)
        self.world_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.world_socket.bind(addresse)
        self.world_socket.listen(1)
        self.client_connection, self.client_adresse = self.world_socket.accept()
        threading.Thread(None,self.recv_msg_c).start()


        
        
        


    def recv_msg_c(self):
        while True:  
            try:
                packet = self.client_connection.recv(1024).decode()
                if packet != "":
                    print("Client: " + packet)
                    self.my_socket.send(packet.encode())
            except:
                break
            
                

        
        
    def recv_msg_s(self):
        while  True:
            packet = self.my_socket.recv(1024).decode()
            if packet != "":
                print("Server: " + packet)
                if packet[:3] == "AXK":
                    threading.Thread(None,self.connection_to_world).start()
                    self.client_connection.send("AXK7?000001bwZa369f58\x00".encode())
                    self.client_socket.close()
                    self.my_socket.close()
                    self.my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    ip = self.hash.decrypt_IP(packet[3:11])
                    self.my_socket.connect((ip,5555))
                else:
                    try:
                        self.client_connection.send(packet.encode())
                    except:
                        pass
                        
                

            





if __name__ == "__main__":
    fr = LeafMITM(("34.251.172.139",5555))