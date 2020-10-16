from character.spell import Spells
from character.deplacement import Deplacement
from map.map import Map


class Character():

    def __init__(self,interface, socket_to_server):
        self.isharvest = False
        self.isfighting = False
        self.spells = Spells(interface)
        self.map = Map(interface)
        self.interface = interface
        self.socket_to_server = socket_to_server
        self.deplacement = Deplacement(self.socket_to_server)
        self.entity = None
        
    def set_cell(self, cell):
        self.cell = cell


    
    def base(self,id_,pseudo,lvl,id_class,sexe,gfx):
        self.id_, self.pseudo, self.lvl, self.id_class, self.sexe, self.gfx = id_, pseudo, lvl, id_class, sexe, gfx


    def character_stats(self,data):
        self.xp_actuelle = data[0].split(",")[0]
        self.xp_depart = data[0].split(",")[1]
        self.xp_fin = data[0].split(",")[2]

        self.kamas = data[1]

        self.points_sorts = data[2]

        self.vie_actuelle = data[5].split(",")[0]
        self.vie_max = data[5].split(",")[1]

        self.ennergie_actuelle = data[6].split(",")[0]
        self.ennergie_max = data[6].split(",")[1]

        self.PA = data[9].split(",")[4]
        self.PM = data[10].split(",")[4]
        
        carac = data[11].split(",")
        self.force = int(carac[0]) + int(carac[1]) + int(carac[2]) + int(carac[3])

        carac = data[12].split(",")
        self.vita = int(carac[0]) + int(carac[1]) + int(carac[2]) + int(carac[3])


        carac = data[13].split(",")
        self.sagesse = int(carac[0]) + int(carac[1]) + int(carac[2]) + int(carac[3])


        carac = data[14].split(",")
        self.chance = int(carac[0]) + int(carac[1]) + int(carac[2]) + int(carac[3])


        carac = data[15].split(",")
        self.agi = int(carac[0]) + int(carac[1]) + int(carac[2]) + int(carac[3])


        carac = data[16].split(",")
        self.intel = int(carac[0]) + int(carac[1]) + int(carac[2]) + int(carac[3])


        carac = data[17].split(",")
        self.PO =int(carac[0]) + int(carac[1]) + int(carac[2]) + int(carac[3])
