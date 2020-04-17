
from character.character import Character
from interface.main_interface import Interface
from character.spells import Spells

class Gestion_Packet():
    
    def __init__(self):
        self.interface = Interface()
    
    def gestion(self,packets):
        
        for packet in packets.split("\x00"):
            print(packet)
            if packet[:3] == "ASK":
                info_perso = packet[3:].split("|")
                self.character = Character(id_ = info_perso[1],pseudo = info_perso[2],lvl = info_perso[3],id_class = info_perso[4],sexe = info_perso[5],gfx = info_perso[6])
                self.interface.create_charater(self.character.gfx,self.character.pseudo,self.character.id_,self.character.lvl)
            
            elif packet[:2] == "SL":
                spells_data = packet[2:].split(";")
                self.spells = Spells(self.interface,spells_data)

            elif packet[:2] == "As":
                self.character.character_stats(packet[2:].split("|"))
                self.interface.base_start(self.character)
                self.interface.create_label_caracteristique(self.character)
        
        
        