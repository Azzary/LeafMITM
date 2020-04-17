import threading
from tkinter import *
from tkinter import ttk


class Map():

    def __init__(self,onglet_map):
        self.onglet_map = onglet_map
        self.create_grille()


    def refresh_map(self,packet):
        data = packet.split("|")

        map_id = int(data[0])
        decrip_key = data[2]

        dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "maps/" + mapId + ".xml")
        tree = etree.parse(dir_path)
        
        if (os.path.isfile(dir_path)):
            for maps in tree.xpath("/RECORD"):
                mapWidth = int(maps.find("ANCHURA").text)
                mapHeight = int(maps.find("ALTURA").text)
                X = int(maps.find("X").text)
                y = int(maps.find("Y").text)
                map_data = maps.find("MAPA_DATA").text
                Decompress_map(map_data)

        
    def Decompress_map(self,map_data):
        celdas = 0
        cell_values = str()
        while i < len(map_data):
            cell_values = map_data[i:10]
            #celdas[i / 10] = descompimir_Celda(cell_values, int((i/10))
        
            
    def create_grille(self):
        Terrain=Canvas(self.onglet_map,height=600,width=600)
        Terrain.place(relx=0.1, rely=0.07, relwidth=0.85, relheight=0.75)
        carreau=[[Terrain.create_rectangle(i*30,j*30,(i+1)*30,(j+1)*30,fill="#FFFFFF")
        for i in range(20)] for j in range(20)]

        #Terrain.bind('<ButtonRelease>',clic)

        #Coord=Label(onglet_map)
        #Coord.pack(pady='10px')



