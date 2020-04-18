import socket
import time
import threading
from gestion_packet import Gestion_Packet
import  hash



class LeafMITM():
    
    def __init__(self,addresse):
        self.gestion_packet = Gestion_Packet()
        self.my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.addresse = ("127.0.0.1",443)
        try:
            self.connection_to()
            self.my_socket.connect(addresse)
        except socket.error:
            print ("connection failed")
        threading.Thread(None,self.recv_msg_s).start()
        #threading.Thread(None,self.send_packet).start()

    def send_packet(self):
        while True:
            packet = input("")
            self.my_socket.send((packet+"\x00").encode())

    
    def connection_to(self):
        self.client_socket.bind(self.addresse)
        self.client_socket.listen(2)
        self.client_connection, self.client_adresse = self.client_socket.accept()
        threading.Thread(None,self.recv_msg_c).start()
        
    
    def switch_serveur(self,packet):
        self.addresse = ("127.0.0.1",5555)
        self.client_socket.close()
        self.client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        threading.Thread(None,self.connection_to).start()
        self.my_socket.close()
        self.my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client_connection.send("AXK7?000001bwZa369f58\x00".encode())
        ip = hash.decrypt_IP(packet[3:11])
        self.my_socket.connect((ip,5555))
    
    def recv_msg_c(self):
        while True:
            packets = self.client_connection.recv(4096).decode()
            for packet in packets.split("\x00"):
                if packet != "":
                    try:
                        packet = self.gestion_packet.gestion_client(packet)
                        packet += "\x00"  
                        self.my_socket.send(packet.encode())
                    except:
                        break
            
    def recv_msg_s(self):
        
        while  True:
            packets = self.my_socket.recv(4096).decode()
            for packet in packets.split("\x00"):
                if packet != "":
                    if packet[:3] == "AXK":
                        self.switch_serveur(packet)
                    else:
                        packet =  self.gestion_packet.gestion_server(packet)
                        packet += "\x00"
                        try:
                            self.client_connection.send(packet.encode())
                        except:
                            pass
                        
                
           





if __name__ == "__main__":
    Leaf_mitm = LeafMITM(("34.251.172.139",5555))