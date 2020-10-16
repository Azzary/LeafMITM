from character.path_finding import *
import time, random
class Combat:

    def __init__(self, map_frame):
        self.map_frame = map_frame

    def mouv_start_cell(self, packet):
        packet = packet[4:].split(";") 
        entity_id = int(packet[0])
        cell = packet[1]
        #??equipe = packet[3]
        self.map_frame.entity_gestion.update_entity(entity_id, int(cell))
    

    def update_carac_entity(self, packet):

        for data in packet[4:].split("|"):
            data = data.split(";")
            entity_id = data[0]
            #il est en vie
            if data[1] == "0":
                vie = data[2]
                pa = data[3]
                pm = data[4]
                cell_id = data[5]
                vie_max = data[7]
                self.map_frame.entity_gestion.update_carac_entity(entity_id,vie,pa,pm,cell_id,vie_max)

    def fight(self):
        time.sleep(random.uniform(0,1.5))
        pos_player =from_cell_id_to_x_y_pos(self.map_frame.character.cell.CellID, self.map_frame.character.map.mapswidth)
        dist = 999999
        
        for noob in self.map_frame.entity_gestion.entity:
            if noob.id == int(self.map_frame.character.id_):
                continue
            pos_entity = from_cell_id_to_x_y_pos(int(noob.cell), self.map_frame.character.map.mapswidth)
            x = heuristic(pos_entity,pos_player)
            if x < dist:
                dist = x
                if pos_entity[1]%2 ==0 and pos_player[1] %2!=0:
                    dist+=0.5
                elif pos_entity[1]%2 !=0 and pos_player[1] %2==0:
                    dist+=0.5
                good_pos = pos_entity
        
        
        
        
        lauch_spell_before = True
        if dist <= 8:
            lauch_spell_before = False
            pos_entity = good_pos
            dist = 0
            for cell in self.map_frame.character.map.cells:
                if cell.isActive:
                    cell_test = from_cell_id_to_x_y_pos(cell.CellID, self.map_frame.character.map.mapswidth)
                    x = heuristic(cell_test, pos_entity)
                    if dist < x:
                        good_pos = cell_test
                        dist = x

        if self.map_frame.character.PM:
            pm = int(self.map_frame.character.PM)
            if lauch_spell_before:
                good_pos = from_pos_x_y_to_cell_id(good_pos[0], good_pos[1], self.map_frame.character.map.mapswidth)
            
                self.map_frame.character.deplacement.deplacement(self.map_frame.character.cell.CellID, good_pos, self.map_frame.character.map.mapswidth, self.map_frame.character.map.carreau, self.map_frame.character.map.binairemap, self.map_frame.character.map.sun, self.map_frame.character.map.resource, pm, True)
                self.launch_spell()
            else:

                self.launch_spell()
                good_pos = from_pos_x_y_to_cell_id(good_pos[0], good_pos[1], self.map_frame.character.map.mapswidth)
            
                self.map_frame.character.deplacement.deplacement(self.map_frame.character.cell.CellID, good_pos, self.map_frame.character.map.mapswidth, self.map_frame.character.map.carreau, self.map_frame.character.map.binairemap, self.map_frame.character.map.sun, self.map_frame.character.map.resource, pm, True)


        self.map_frame.character.socket_to_server.send((f"Gt"+"\n\x00").encode())

        if False:# dist > 8 and dist not in (1.9142135623730951, 1.5):
            if self.map_frame.character.PM:
                pm = int(self.map_frame.character.PM)
                self.map_frame.character.deplacement.deplacement(self.map_frame.character.cell.CellID, from_pos_x_y_to_cell_id(good_pos[0], good_pos[1], self.map_frame.character.map.mapswidth), self.map_frame.character.map.mapswidth, self.map_frame.character.map.carreau, self.map_frame.character.map.binairemap, self.map_frame.character.map.sun, self.map_frame.character.map.resource, pm, True)
                self.launch_spell()
            for i in range(1,int(self.map_frame.character.PM)*2+2,2):
                    if not int(heuristic(good_pos, pos_entity)-i) < 8//1.5:
                        pm = i//2
                    else:
                        break


    def launch_spell(self,spells_id = (161,163)):
        dist = 99999
        for spell_id in spells_id:

            for noob in self.map_frame.entity_gestion.entity:
                if noob.id == int(self.map_frame.character.id_):
                    continue
                pos_entity = from_cell_id_to_x_y_pos(int(noob.cell), self.map_frame.character.map.mapswidth)
                x = heuristic(pos_entity,from_cell_id_to_x_y_pos(self.map_frame.character.cell.CellID, self.map_frame.character.map.mapswidth))
                if x < dist:
                    dist = x
                    good_pos = noob.cell

            print(f"Lancement du sort {spell_id}, sur la cell {good_pos}")
            self.map_frame.character.socket_to_server.send((f"GA300{spell_id};{good_pos}"+"\n\x00").encode())
            time.sleep(random.uniform(1.2,2.3))



        return
        path = os.getcwd()+"\\resource\\spells.xml"
        for spell in spells_id:
            for spell in tree.xpath("/SPELLS/SPELL"):
                if spell == spell.get("ID"):
                    spell_name = spell.get("ID").get("LEVEL")
                    print(spell_name)
                
                for noob in self.map_frame.entity_gestion.entity:
                    pass




if __name__ == "__main__":
        import os
        from lxml import etree
        spells_id = (161,163)
        path = os.getcwd()+"\\resource\\spells.xml"
        tree = etree.parse(path)
        for spell in spells_id:
            for spell in tree.xpath("/SPELLS/SPELL"):
                if "151" == spell.get("ID"):
                    spell_name = spell.get("ID").get("LEVEL").text
                    print(spell_name)
