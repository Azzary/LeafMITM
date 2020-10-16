from character.character import Character
from map.map_frame import MapFrame
from map.combat import Combat
import threading
from script import Script

class PacketGestion():

    def __init__(self, interface, socket_to_server):
        self.character = Character(interface, socket_to_server)
        self.interface = interface
        self.socket_to_server = socket_to_server
        self.interface.set_character(self.character)
        self.map_frame = MapFrame(interface, self.character)
        self.combat = Combat(self.map_frame)
        self.script = Script(self.character)

    def set_socket(self, socket_to_server):
        self.socket_to_server = socket_to_server
        self.character.set_socket(self.socket_to_server)
        #self.interface.ongletsMap.set_socket(self.socket_to_server)

    def server_packet(self, packet):

        #character information
        if packet[:3] == "ASK":
            info_perso = packet[3:].split("|")
            self.character.base(id_ = info_perso[1],pseudo = info_perso[2],lvl = info_perso[3],id_class = info_perso[4],sexe = info_perso[5],gfx = info_perso[6])
            self.interface.ongletsPersonnage.create_charater(self.character.gfx,self.character.pseudo,self.character.id_,self.character.lvl)
        #spell   (lvl,available spell...)
        elif packet[:2] == "SL" and packet[2:4] != "o+":
            spells_data = packet[2:].split(";")
            self.character.spells.update_spells(spells_data)
        #character stats (all stats pa, pm, res fix, rex....)
        elif packet[:2] == "As":
            self.character.character_stats(packet[2:].split("|"))
            self.interface.base_start(self.character)
            #self.map_frame.player_id = self.character.id_
            self.interface.ongletsPersonnage.create_label_caracteristique(self.character)

        #map information (mapid, date of creation,key)
        elif packet[:3] == "GDM":
                data = packet.split("|")
                mapID = data[1]
                map_date = data[2]
                decryption_key = data[3]
                self.character.map.data(mapID, map_date, decryption_key)
                self.interface.ongletsMap.print_map(self.character.map)
        #entity map information
        elif packet[:2] == "GM":
            self.map_frame.parse_data(packet)
        elif packet[:3] == "GDF" and len(packet) > 7:
            self.map_frame.update_interactive(packet)
        elif self.character.entity:
            if packet[:2] == "GA":
                self.map_frame.update_entity(packet)
            elif packet[:3] == "GIC":
                self.combat.mouv_start_cell(packet)
            elif packet[:2] == "GE":
                self.character.isfighting = False
            elif packet[:3] == "GTM":
                self.combat.update_carac_entity(packet)          
            elif packet[:3] == "GTS":
                data =  packet[3:].split("|")
                if data[0] == self.character.id_:
                    print("debut du tour...")
                    threading.Thread(None,self.combat.fight).start()
                    

   


