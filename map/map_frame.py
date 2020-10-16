import time, threading
from entity.entity import Entity
from resource.hash import get_Cell_Id_From_Hash
from map.entity_gestion import EntityGestion


class MapFrame():

    def __init__(self, interface, character = None):
        self.entity_gestion = EntityGestion(interface)
        self.character = character
        


    def parse_data(self, packet):
        instances = packet[3:].split('|')
        for instance in instances:
            if len(instance) < 1:
                continue
            if instance[0] == '+':
                infos = instance[1:].split(';')
                if len(infos) < 6:
                    continue

                cell = int(infos[0])
                template = infos[4]
                try:
                    type_ = int(infos[5]) if ',' not in infos[5] else int(infos[5].split(',')[0])
                except:
                    continue
                
                entity_id = int(infos[3])

                # SWITCH
                if type_ == -1:  # creature
                    pass
                elif type_ == -2:  # mob
                    # if not self.character_state.isFighting:
                    #    return
                    #monster_team = infos[15] if len(infos) <= 18 else infos[22]
                    levels = list(map(int, infos[7].split(',')))
                    if len(infos) == 12:
                        self.entity_gestion.add_entity(Entity('Mob', cell=cell, id=entity_id, template=template, pa=infos[12], vie=infos[13], pm=infos[14]))
                    else:
                        self.entity_gestion.add_entity(Entity('Mob', cell=cell, id=entity_id, template=template, pa=None, vie=None, pm=None))
                    #self.entities.append(Entity('Mob', cell=cell, id=entity_id, template=template, pa=infos[12], vie=infos[13], pm=infos[14]))
                elif type_ == -3:  # group of mob
                    templates = list(map(int, template.split(',')))
                    levels = list(map(int, infos[7].split(',')))
                    entity_id = int(infos[3])

                    self.entity_gestion.add_entity(Entity('GroupMob', cell=cell, id=entity_id, templates=templates, levels=levels))
                elif type_ == -4:  # NPC
                    pass  # map.entities.add(id, Npc(id, int(nombre_template), cell))
                elif type_ == -5:  # Merchants
                    pass  # map.entities.add(id, Mercantes(id, cell))
                elif type_ == -6:  # resources
                    pass
                else:  # players
                    if entity_id != int(self.character.id_):
                        self.entity_gestion.add_entity(Entity('Player', cell=cell, id=entity_id, name=infos[4], pa=None, vie=None, pm=None))
                    else:
                        self.entity_gestion.add_entity(Entity('Player', cell=cell, id=entity_id, name=infos[4], isMainCharacter = True, pa=None, vie=None, pm=None))
            
            elif instance[0] == '-':  # player leave
                entity_id = int(instance[1:])
                
                self.entity_gestion.update_entity(entity_id,None)

    def update_entity(self, packet):
        if packet[:4] == "GA;0" or packet[:3] == "GAS" or packet[:3] == "GAF":
            return
        data = packet[2:].split(";")
        action_id = int(data[1])
        entity_id = int(data[2])
        #Travel on the map
        if action_id == 1:
            end_cell = get_Cell_Id_From_Hash(data[3][len(data[3]) - 2:])
            if entity_id == int(self.character.id_):
                pass
            self.entity_gestion.update_entity(entity_id, end_cell)
        #Le personnage recolte
        elif action_id == 501:
            
            harvest_time = int(data[3].split(",")[1]) / 1000
            cell_id = data[3].split(",")[0]
            type_of_harvest = data[0]
            if entity_id == int(self.character.id_):

                threading.Thread(None,self.is_having,args=(harvest_time,cell_id)).start()
        #combat
        elif action_id == 905:
            if entity_id == int(self.character.id_):
                self.character.isfighting = True
                #self.character.map.data(mapID, map_date, decryption_key)
                self.entity_gestion.remove_all_entity(self.character.map)
                self.character.interface.ongletsMap.print_map(self.character.map)
                 
        #entity pousser
        elif action_id == 5:
            data_entity_cible = data[3].split(",")
            self.entity_gestion.update_entity(int(data_entity_cible[0]),int(data_entity_cible[1])) 
        elif action_id == 103:
            if self.character.isfighting:
                id_du_mort = int(data[3])
                self.entity_gestion.update_entity(id_du_mort, None) 
    def is_having(self,harvest_time,cell_id):
        self.character.isharvest = True
        print(f"Le personnage recolte un resource sur la cellid {cell_id} temps d'attente {str(harvest_time)} s")
        time.sleep(harvest_time)
        self.character.isharvest = False
        


    def update_interactive(self, packet):
        cells_id = []
        for data in packet[4:].split("|"):
            
            data = data.split(";")
            cell_id = int(data[0])
            action = int(data[1])

            
            if action == 2:
                self.entity_gestion.update_interactive(cell_id)
            elif action == 3:
                self.entity_gestion.update_interactive(cell_id)
                """
                if the character harvests:
                    pass
                else:
                    pass resource steal
                """
            elif action == 4: #need to leave the map to be able to interact with
                self.entity_gestion.update_interactive(cell_id)
            elif action == 5: #Can recolte 
                self.entity_gestion.update_interactive(cell_id, True)
            cells_id.append(cell_id)
            
        return cells_id
