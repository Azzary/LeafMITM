import yaswfp.swfparser as swfparser
from map_gestion.pos import MAPID_TO_POS
from urllib.parse import unquote
from map_gestion.contants import *
from map_gestion.entity import Entity
from map_gestion.cell import Cell

from map_gestion.collection import Collection
#from utils.entity import Entity
#from utils.collection import Collection

# source https://github.com/XeLiT


class Map():
    
    def __init__(self, id, date, raw_key):
        self.entity = None
        MAP_DIR = "D:/Users/remic/Desktop/myprojet/retroclient/data/maps"
        self.path = '{}/{}_{}{}.swf'.format(MAP_DIR, id, date, 'X' if raw_key else '')
        pos = MAPID_TO_POS[id]
        self.x = pos[0]
        self.y = pos[1]
        swf = swfparser.parsefile(self.path)
        raw_map_data = swf.tags[2].Actions[0].ConstantPool[14]
        self.width = int(swf.tags[2].Actions[17].Integer)
        self.height = (int(swf.tags[2].Actions[20].Integer) - 1) * 2
        data = self.decrypt_mapdata(raw_map_data, raw_key)
        cellid = []
        for i in range(0, len(data), 10):
            raw_cells = data[i:i+10]
            cellid += [int(i/10)]
        cellid += [int(cellid[-1]+1)]
        raw_cells = [data[i:i+10] for i in range(0, len(data), 10)]
        self.cells = [Cell(raw_cells[i],cellid[i]) for i in range(len(raw_cells))]

                    
    
    def decrypt_mapdata(self, raw_data, raw_key):
        key = unquote(''.join([chr(int(raw_key[i:i+2], 16)) for i in range(0, len(raw_key), 2)]))
        checksum = int(HEX_CHARS[sum(map(lambda x: ord(x) & 0xf, key)) & 0xf], 16) * 2
        key_length = len(key)
        data = ''
        for i in range(0, len(raw_data), 2):
            data += chr(int(raw_data[i:i+2], 16) ^ ord(key[(int(i / 2) + checksum) % key_length]))
        return data
        
        
    def matrixfy(self) -> [[Cell]]:
        rows = []
        i = 0
        row_number = 0
        while row_number < self.height:
            if row_number % 2 == 0:
                take = self.width -1
                rows.append(self.cells[i:i+take])
                i += take
            else:
                take = self.width 
                rows.append(self.cells[i:i+take])
                i += take
            row_number += 1
        return rows
      
    def change_colors(entity):
        pass
          
    def remove_entities(self):
        for c in self.cells:
            c.set_entity(None)

    def place_entities(self, entities: [Entity]):
        indexed_by_cell = Collection(entities).index_by('cell')
        for cell in indexed_by_cell.keys():
            self.cells[int(cell)].set_entity(indexed_by_cell[cell])
            self.cells[int(cell)].color = "red"
            #self.table.set_data(self.map.matrixfy())