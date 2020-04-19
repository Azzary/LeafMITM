from map_gestion.entity import Entity

class Map_Frame():
    
    def __init__(self, raw_data,_map, entitie):
        self.entities = entitie
        self.map = _map
        self.action = '+'
        self.parse_data(raw_data)


    def __repr__(self):
        return '\n'.join(map(str, self.entities)) if len(self.entities) else ''

    def parse_data(self, data):
        instances = data[3:].split('|')
        for instance in instances:
            if len(instance) < 1:
                continue
            if instance[0] == '+':
                infos = instance[1:].split(';')
                cell = int(infos[0])
                template = infos[4]
                type = int(infos[5]) if ',' not in infos[5] else int(infos[5].split(',')[0])
                entity_id = int(infos[3])

                # SWITCH
                if type == -1:  # creature
                    pass
                elif type == -2:  # mob
                    # if not self.game_state.isFighting:
                    #    return
                    # monster_team = infos[15] if len(infos) <= 18 else infos[22]
                    self.entities.append(Entity('Mob', cell=cell, id=entity_id, template=template, pa=infos[12], health=infos[13], pm=infos[14]))
                elif type == -3:  # group of mob
                    templates = list(map(int, template.split(',')))
                    levels = list(map(int, infos[7].split(',')))
                    entity_id = int(infos[3])
                    self.entities.append(Entity('GroupMob', cell=cell, id=entity_id, templates=templates, levels=levels))
                elif type == -4:  # NPC
                    pass  # mapa.entidades.TryAdd(id, new Npc(id, int.Parse(nombre_template), celda))
                elif type == -5:  # Merchants
                    pass  # mapa.entidades.TryAdd(id, new Mercantes(id, celda))
                elif type == -6:  # resources
                    pass
                else:  # players
                    self.entities.append(Entity('Player', cell=cell, id=entity_id, name=infos[4]))
                    
                self.map.place_entities(self.entities)
                
                
            elif instance[0] == '-':  # player leave
                entity_id = int(instance[1:])
                self.action = '-'
                for entity in self.entities:
                    try:
                        if entity.id == entity_id:
                            self.entities.remove(entity)
                            self.map.remove_entities(self.entities)
                            break
                    except:
                        continue
                
                    
        