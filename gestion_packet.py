
from character.character import Character
from interface.main_interface import Interface
from character.spells import Spells
from map_gestion.map import Map
from map_gestion.map_frame import Map_Frame


class Gestion_Packet():
    
    def __init__(self):
        self.interface = Interface()
        self.map = None
        self.entitie = []
    def gestion_server(self,packet):
        #print("Server:" + packet)
        self.interface.print_richTextBox1("Server:" + packet)
        #character information
        if packet[:3] == "ASK":
            info_perso = packet[3:].split("|")
            self.character = Character(id_ = info_perso[1],pseudo = info_perso[2],lvl = info_perso[3],id_class = info_perso[4],sexe = info_perso[5],gfx = info_perso[6])
            self.interface.create_charater(self.character.gfx,self.character.pseudo,self.character.id_,self.character.lvl)
        #spell   (lvl,available spell...)
        elif packet[:2] == "SL":
            spells_data = packet[2:].split(";")
            self.spells = Spells(self.interface,spells_data)
        #character stats (all stats pa, pm, res fix, rex....)
        elif packet[:2] == "As":
            self.character.character_stats(packet[2:].split("|"))
            self.interface.base_start(self.character)
            self.interface.create_label_caracteristique(self.character)
        #map information (mapid, date of creation,key)
        elif packet[:3] == "GDM":
                data = packet.split("|")
                self.mapID = data[1]
                self.map_date = data[2]
                self.decryption_key = data[3]
                self.entitie = []
                self.map = Map(self.mapID, self.map_date, self.decryption_key)
                self.interface.update_map(self.map)
        #character pods
        elif packet[:2] == "Ow":
                data = packet[2:].split("|")
                pods_actu = data[0]
                pods_max = data[1]
        #entity map information
        elif packet[:2] == "GM":
            #print(packet)
            entity = Map_Frame(packet,self.map, self.entitie)
            self.entitie.append(entity)
            self.interface.update_entity(self.entitie)
            
            
            #self.interface.update_map(self.map)
                          
                
                
        return packet
     
     
     
                   
    def gestion_client(self,packet):
        #print("Client: "+packet)
        self.interface.print_richTextBox1("Client:" + packet)
        return packet
                
            
        
        