import threading
from tkinter import *
from tkinter import ttk
from map_gestion import map
from interface.table import Table

# source https://github.com/XeLiT

class MapInterface():

    def __init__(self,onglet_map):
        
        self.map: Map = None
        self.lastMap = None
        self.playerCell = 0
        self.isFighting = False
        self.entities = []
        self.map_id = 0
        
        
        self.onglet_map = onglet_map
        self.table = None
        self.init_table(19, 42)


    def init_table(self, width, height):
        if self.table:
            self.table.pack_forget()
            self.table.destroy()
        self.table = Table(self.onglet_map, rows=height, columns=width)
        self.table.grid(row=1, column=1, rowspan=height)    
        
        
    def update_map(self, map_change):
        self.entities = []
        self.lastMap = self.map
        self.map = map_change
        
        self.init_table(self.map.width, self.map.height)
        self.update()
    
    def update_entity(self, entities):
         
        self.table.set_entities(entities)
        
    def update(self):
        if self.map:
            self.table.set_data(self.map.matrixfy())