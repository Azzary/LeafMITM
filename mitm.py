from threading import Thread
import socket, time, fritm
from interface.main_interface import MainInterface
from protocol.packet_gestion import PacketGestion
from map.contants import PATH

class MITM():
    def __init__(self,server_ip = "127.0.0.1",server_port = 6555, interface = None, packet_gestion = None):
        self.server_port = server_port
        self.server_ip = server_ip
        self.interface = interface
        self.socket_to_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_to_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.interface == None: 
            self._hook()
            self.interface = MainInterface()
        self.packet_gestion = PacketGestion(self.interface, self.socket_to_server)
        self.start_client()


    def start_client(self):
        try:
            self.socket_to_client.bind((self.server_ip,self.server_port))
        except:
            print(f"Can't blind for the client")

        self.socket_to_client.listen(1)
        self.connexion, adresse = self.socket_to_client.accept()
        print("connection made...\nconnection to server")
        
        self.listening_client()


    def start_server(self,adresse):
        try:
            self.socket_to_server.connect((adresse[0],int(adresse[1])))
            self.connexion.send((f"HTTP/1.0 200 OK").encode())
            time.sleep(0.5)
        except:
            print(f"Can't blind the server")

        #listening_server
        Thread(None,self._boucle_recv_send,args = [self.socket_to_server, self.connexion, "Server: "]).start()    


    def listening_client(self):
        #packet contains the true ip and port 
        packet = self.connexion.recv(1024).decode()
        packet = packet.split(" ")[1].split(":")
        self.start_server(packet)
        self._boucle_recv_send( self.connexion, self.socket_to_server, "Client: ")                  
        self._switch_server()

    def _switch_server(self):
        self.socket_to_server.close()
        self.socket_to_client.close()
        self.connexion.close() 
        Thread(None,self.__init__,args = [self.server_ip,self.server_port, self.interface, self.packet_gestion]).start()    

    def _hook(self):
        fritm.spawn_and_hook((PATH+"/Dofus.exe"), 6555)        
        self.httpd = fritm.start_proxy_server(None)

    def _boucle_recv_send(self, recv, send, source, packets = None):
        while packets != "":
            try:
                packets = recv.recv(1024)
                send.send(packets)
            except:
                break
            packets = packets.decode()
            if source == "Client: ":
                if packets[:5] == "GA001":
                    print(packets.split())
            for packet in packets.split("\x00"):
                Thread(None,self.interface.ongletsPackets.print_packet,args = [(source + packet)]).start() 
                if source == "Server: ": 
                    self.packet_gestion.server_packet(packet)  

  

            
        recv.close()
        print("close connection with a "+ source) 

if __name__ == "__main__":
    MITM()