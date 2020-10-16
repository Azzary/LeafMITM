

import copy

class EntityGestion():

    def __init__(self, interface):
        self.map = interface.ongletsMap
        self.character = self.map.character
        self.entity = []



    def remove_all_entity(self,map):
        self.entity = []
        for cell in map.cells:
            cell.entity = []
            cell.set_default_color()
                    
    def add_entity(self, entity):
        cell = self.map.carreau[entity.cell]
        if entity in cell["cell"].entity:
            self.remove_entity(cell,entity)
        cell["cell"].set_entity(entity, True)
        self.map.Terrain.itemconfigure(cell["carreau"], fill=cell["cell"].color)
        if self.character.id_ == str(entity.id):
            self.character.set_cell(cell["cell"])
            self.character.entity = entity 
        self.character.map.entity.append(entity)
        self.entity.append(entity)


    def remove_entity(self,cell, entity):
        cell["cell"].set_entity(entity, False)
        self.map.Terrain.itemconfigure(cell["carreau"], fill=cell["cell"].color)
        self.character.map.entity.remove(entity)
        self.entity.remove(entity)


    def update_entity(self, entity_id, end_cell, update_cara = False):
        for cle,cell in self.map.carreau.items():
            if cell["cell"].entity != []:
                entity = cell["cell"].get_entity(entity_id)
                if entity:
                    if update_cara:
                        return entity
                    self.remove_entity(cell,entity)
                    if end_cell:
                        entity.cell = end_cell
                        self.add_entity(copy.copy(entity))
                    

    def update_carac_entity(self,entity_id,vie,pa,pm,cell_id,vie_max):
        entity = self.update_entity(int(entity_id), int(cell_id), True)
        if entity:
            entity.vie = vie 
            entity.pa = pa
            entity.pm = pm
            entity.cell = cell_id
            print(entity.__dict__)

    def update_interactive(self,cell_id, good = False):
        cell = self.map.carreau[cell_id]
        cell["cell"].set_not_interactive(good)
        self.map.Terrain.itemconfigure(cell["carreau"], fill=cell["cell"].color)
        #self.character.map.resource.append(cell_id)