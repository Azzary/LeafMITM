import tkinter, time , copy, threading
import time
import character.job as job

class OngletsMap():

    def __init__(self, main_onglets):
        self.onglet_map = tkinter.ttk.Frame(main_onglets)      
        self.onglet_map.pack()
        main_onglets.add(self.onglet_map, text='map')
        self.size_carreau = 20
        self.Terrain = tkinter.Canvas(self.onglet_map)
        self.carreau = {}

    def set_character(self, character):
        self.character = character

    def print_map(self, maps):
        self.Terrain.destroy()
        self.carreau = {}
        self.Terrain = tkinter.Canvas(self.onglet_map,height = self.size_carreau * (maps.height)*2, width = self.size_carreau * (maps.width)*2)
        self.binairemap = []
        self.mapswidth = maps.width
        self.Terrain.place(x = 5, y = 5)
        self.getcell = []
        i = -1
        j = 0
        liste = []
        liste2 = []
        self.sun = []
        self.resource = []
        for cell in maps.cells:
            if i >= maps.width:
                j += 1
                i = 0
                self.getcell.append(liste)
                self.binairemap.append(liste2)
                liste2 = []
                liste = []
            if i == 0 and j%2 == 0:
                if j != 0 and j%2 ==0:
                    liste2.append(1)
                self.Terrain.create_rectangle(i*self.size_carreau*2,j*self.size_carreau,(i+1)*self.size_carreau*2,(j+1)*self.size_carreau,fill = "black")
                #liste.append({str(cell.CellID):self.Terrain.create_rectangle(i*self.size_carreau*2,j*self.size_carreau,(i+1)*self.size_carreau*2,(j+1)*self.size_carreau,fill = "black"),"cell":None})
                
                i += 1
            elif i == 0:
                i = 0.5
            self.create_binary_map(cell,liste2)
            self.carreau[cell.CellID] = {"carreau":self.Terrain.create_rectangle(i*self.size_carreau*2,j*self.size_carreau,(i+1)*self.size_carreau*2,(j+1)*self.size_carreau,fill = cell.color), "cell" :cell}

            liste.append(cell.CellID)
            
            #liste.append({cell.CellID:self.Terrain.create_rectangle(i*self.size_carreau*2,j*self.size_carreau,(i+1)*self.size_carreau*2,(j+1)*self.size_carreau,fill = cell.color),"cell":cell})
            i += 1
        self.Terrain.bind('<ButtonRelease>',self.clic)

        Coord = tkinter.Label(self.onglet_map)
        Coord.pack(pady='10px')
        maps.binairemap = self.binairemap
        maps.carreau = self.carreau
        maps.mapswidth = self.mapswidth
        maps.sun = self.sun
        maps.resource = self.resource

    def create_binary_map(self,cell,liste2):
        if cell.color == 'yellow':
                self.sun.append(cell.CellID)
        if cell.color == 'white':
            liste2.append(0)
        else:
            type_recolte = job.get_id(cell.layerObject2Num)
            if type_recolte and type_recolte[2] in ("Cueillir","Faucher"):
                liste2.append(0)
                self.resource.append(cell.CellID)
            else:
                liste2.append(1)


    def clic(self, event):
        i=event.y//(self.size_carreau)
        if i%2 != 0:
            j = int((event.x-self.size_carreau)//self.size_carreau//2)
        else:
            j = event.x//(self.size_carreau)//2
            j-= 1
        cell_ID = self.getcell[i][j]
        if self.carreau[cell_ID]:
            #print(self.carreau[cell_ID]["cell"].__dict__)
            if self.carreau[cell_ID]["cell"].isInteractive:
                job.recole(self.character,cell_ID)
            elif not self.character.deplacement.ismouving and not self.character.isharvest:
                self.character.deplacement.deplacement(self.character.cell.CellID, cell_ID, self.mapswidth, self.carreau, self.binairemap, self.sun, self.resource)
            else: print("Deja en mouvement...")




