
from character.character import Character
from interface.main_interface import Interface
from character.spells import Spells
from map_gestion.map import Map
from map_gestion.map_frame import Map_Frame
import hash
from copy import copy

class Gestion_Packet():
    
    def __init__(self):
        self.interface = Interface()
        self.map = None
        self.entitie = []
        self.map_frame = None
        
    def gestion_server(self,packet):
        self.entitie_remove = []
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
            self.map_frame = Map_Frame(packet,self.map, self.entitie,self.character.id_)
            self.entitie = self.map_frame.entities
            self.entitie_remove = self.map_frame.entities_remove
            #Enlever les try:exp... probleme avec les entities reglée 
            self.interface.update_entity(self.entitie, self.entitie_remove)
        elif packet[:2] == "GA":
            print(packet)
            if packet != "GA;0":
                data = packet[2:].split(";")
                action_id = int(data[1])
                entity_id = int(data[2])
                
                #Travel on the map
                if action_id == 1:
                    cell = hash.get_Cell_Id_From_Hash(data[3][len(data[3]) - 2:])
                    for i in range(len(self.entitie)):
                        if entity_id == self.entitie[i].id:
                            self.entitie_remove.append(copy(self.entitie[i]))
                            self.entitie[i].cell = cell
                            
                    if  self.map_frame != None:
                        self.map_frame.update_entity(self.entitie,self.entitie_remove)
                        self.entitie = self.map_frame.entities
                        self.entitie_remove = self.map_frame.entities_remove
                        
                        self.interface.update_entity(self.entitie, self.entitie_remove)

                          
                
                
        return packet
     
     
     
                   
    def gestion_client(self,packet):
        #print("Client: "+packet)
        self.interface.print_richTextBox1("Client:" + packet)
        return packet


            
        
        